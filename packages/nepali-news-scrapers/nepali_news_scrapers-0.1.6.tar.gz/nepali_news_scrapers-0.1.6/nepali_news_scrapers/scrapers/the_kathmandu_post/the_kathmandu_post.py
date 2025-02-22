import os
import re
import requests
import time
import json
import logging
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from services.scraper_service import ScraperService


class KathmanduPostScraper:
    def __init__(self,scraper_service:ScraperService):
        self.base_url = "https://kathmandupost.com"
        self.service = scraper_service
        self.unique_links = set()

    def make_request_url(self, url):
        return self.base_url.strip().rstrip("/") + "/" + url.strip().lstrip("/")

    def start(self):
        self.get_page_listings(self.make_request_url("/latest"))

    def get_page_listings(self, page_url):
        # make a get request to url
        page_content = self.service.make_get_request(page_url)
        if not page_content:
            return

        
        soup = BeautifulSoup(page_content, "html.parser")
        new_links_found = False

        trending_lists = soup.find_all("ul", class_="trending-topics-list")
        if trending_lists:
            for trending_list in trending_lists:
                a_tags = trending_list.find_all("a")
                for a_tag in a_tags:
                    href_links = a_tag.get("href")
                    self.unique_links.add(href_links)
                    new_links_found = True

        # To get list of articles
        a_tags = soup.select("div.block--morenews article.article-image a")
        for a_tag in a_tags:
            href_links = a_tag.get("href")
            self.unique_links.add(href_links)
            new_links_found = True

        if new_links_found:
            self.service.log.info("New links found. Fetching page details...")
            for link in self.unique_links:
                article_link = self.make_request_url(link)
                self.get_page_details(article_link)

    def get_page_details(self, url):
        page_content = self.service.make_get_request(url)
        if not page_content:
            return

        soup = BeautifulSoup(page_content, "html.parser")
        
        # Extract category
        category_text = ""
        category_container = soup.find("h4", {"class": "title--line__red"})
        if category_container:
            anchor_text = category_container.find("a")
            if anchor_text:
                category_text = anchor_text.text.strip()

        # Extract title
        news_title = ""
        title_tag = soup.find("title")
        if title_tag:
            news_title = title_tag.text.strip()

        # Extract subtitle
        title_sub = ""
        title_sub_tag = soup.find("span", {"class": "title-sub"})
        if title_sub_tag:
            title_sub = title_sub_tag.text.strip()

        # Extract Published Date & Time
        date_part, time_part = "", ""
        date_time_container = soup.find_all("div", {"class": "updated-time"})
        if len(date_time_container) > 1:
            date_time = date_time_container[1].text.strip()
            match = re.search(r'(\w+ \d{1,2}, \d{4}) (\d{2}:\d{2})', date_time)
            if match:
                date_part = match.group(1)
                time_part = match.group(2)
                datetime_str = f"{date_part} {time_part}"
                
                try:
                    date_obj = datetime.strptime(datetime_str, "%B %d, %Y %H:%M")
                    date_now = datetime.now()
                    if date_now - date_obj >= timedelta(days=1):
                        self.service.log.info(f"Skipping {url} as it is older than the threshold time/date value")
                        return False
                except ValueError:
                    self.service.log.warning(f"Date parsing failed for {datetime_str}")

        # Extract Author
        author_text = "Unknown"
        author_container = soup.find('a', href=re.compile(r"^/author"))
        if author_container:
            author_text = author_container.text.strip()

        # Extract Content
        content = ""
        content_container = soup.find("section", {"class": "story-section"})
        if content_container:
            content = content_container.text.strip()

        # Compile news data
        news_data = {
            "url": url,
            "title": news_title,
            "category": category_text,
            "author": author_text,
            "published_time": time_part,
            "published_date": date_part,
            "content": content
        }

        # Save to JSON file
        self.service.save_json(news_data,news_title,"the_kathmandu_post")

        


