import os
import requests
from bs4 import BeautifulSoup
import json
import time 
from datetime import datetime , timedelta
import re
from nepali.date_converter import converter
from services.scraper_service import ScraperService





class TheAnnapurnaPostScraper:
    def __init__(self,scraper_service:ScraperService):

        self.base_url = "https://annapurnapost.com"
        self.service = scraper_service
        self.unique_links = set()  # Store links persistently within the class

    def make_request_url(self, url):
        return self.base_url.strip().rstrip("/") + "/" + url.strip().lstrip("/")

    def start(self):
        self.get_page_category()

    def get_page_category(self):
        categories = [
            'editorial', 'apheadline', 'politics', 'opinion', 'social',
            'economy', 'sports', 'video-gallery', 'corporate', 'foreign', 'tech',
            'susashan-special', 'interview', 'health', 'sampurna', 'fursad',
            'image-gallery', 'prabas', 'angkur', 'entertainment', 'art-philosophy',
            'interesting-world', 'npl', "provience1", "provience2", "provience3",
            "provience4", "provience5", "provience6", "provience7", 'latest-news'
        ]
        

        for category in categories:
            try:
                self.service.log.info(f"Scraping Category: {category}")
                page_url = self.make_request_url(f"category/{category}")
                self.get_page_listings(page_url, category)
            except Exception as e:
                self.service.log.error(f"Request failed: {e}")
                continue


    def get_page_listings(self, page_url, category):
        page_num = 1
        while page_num<=2:
            current_page_url = f"{page_url}/?page={page_num}"
            self.service.log.info(f"Scraping page: {current_page_url}")

            page_content = self.service.make_get_request(current_page_url)
            if not page_content:
                break

            soup = BeautifulSoup(page_content, "html.parser")
            grid_cards = soup.find_all("div", class_="grid__card")
            
            # Move the unique links check here, *before* the loop
            new_links_found = False
            for card in grid_cards:
                anchors = card.find_all("a")
                for a in anchors:
                    href = a.get("href")
                    if href and "category" not in href:
                        full_link = self.make_request_url(href)
                        if full_link not in self.unique_links:  # Check if link is unique
                            self.unique_links.add(full_link)
                            self.get_page_details(full_link, category)  # Pass category
                            new_links_found = True
                        else:
                            pass #skipping

            if not new_links_found:
                break

            page_num += 1



    def get_page_details(self, url, category):  # Accept category as argument
        page_content = self.service.make_get_request(url)
        if not page_content:
            return


        soup = BeautifulSoup(page_content, "html.parser")

        title_container = soup.find('h1', class_='news__title')
        title = title_container.text.strip() if title_container else ""

        time_date_container = soup.find('p', class_='date')
        time_date = time_date_container.text.strip() if time_date_container else ""
        date_part, time_part = "", ""
        if time_date:
            try:
                # Split the date and time parts
                date_part, time_part = time_date.rsplit(' ', 1)
            except ValueError:
                self.service.log.warning(f"Unable to split date and time for URL: {url}")

        print("Date and time part as:", date_part, time_part)

        # Mapping Nepali months to their respective numbers
        nepali_month_mapping = {
            'बैशाख': 1, 'जेठ': 2, 'असार': 3, 'साउन': 4, 'भदौ': 5, 'असोज': 6,
            'कात्तिक': 7, 'मंसिर': 8, 'पुष': 9, 'माघ': 10, 'फागुन': 11, 'चैत': 12
        }

        try:
            # Split the date_part into components
            date_components = date_part.split()
            # Extract the first three components (month, date, year)
            nepali_month_str = date_components[0]
            nepali_date_str = date_components[1].strip(',')
            nepali_year_str = date_components[2]

            # Convert Nepali month to number
            nepali_month = nepali_month_mapping.get(nepali_month_str)
            if nepali_month is None:
                raise ValueError(f"Invalid Nepali month: {nepali_month_str}")

            nepali_date = int(nepali_date_str)
            nepali_year = int(nepali_year_str)

            # Convert Nepali date to English date
            en_year, en_month, en_date = converter.nepali_to_english(nepali_year, nepali_month, nepali_date)

            # Extract time components
            nepali_time_str = time_part
            nepali_hour, nepali_minute, nepali_second = map(int, nepali_time_str.split(':'))

            # Create a datetime object for the article
            article_datetime = datetime(en_year, en_month, en_date, nepali_hour, nepali_minute, nepali_second)

            # Get the current datetime
            current_datetime = datetime.now()

            # Compare the datetime objects
            if current_datetime - article_datetime >= timedelta(hours=12):
                self.service.log.info(f"Skipping {url} as it is older than the threshold time/date value")
                return False  # Skip this news link
            else:
                self.service.log.info(f"Processing {url} as it is within the threshold time/date value")
                # Continue processing the news link

        except (ValueError, IndexError, AttributeError) as e:
            self.service.log.error(f"Error parsing date or time for URL {url}: {e}")
            return False  # Skip this news link if there's an error


        author_container = soup.find("p", {"class": "author__name"})
        author = author_container.text.strip() if author_container else ""

        content_container = soup.find("div", {"class": "news__details"})
        content = content_container.text.strip() if content_container else ""

        news_data = {
            "url": url,
            "category": category,
            "title": title,
            "time_date": time_date,
            "published_date": date_part,
            "published_time": time_part,
            "author": author,
            "content": content
        }

        self.service.save_json(news_data,title,"annapurna_post")
