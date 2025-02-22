import os
import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime, timedelta
import re
from nepali.date_converter import converter
from services.scraper_service import ScraperService



class SetoPatiScraper:
    def __init__(self,scraper_service:ScraperService):
        self.base_url = "https://www.setopati.com"
        self.unique_links = set()
        self.service = scraper_service


    
    
    def make_request_url(self, url):
        return self.base_url.strip().rstrip("/") + "/" + url.strip().lstrip("/")

    def start(self):
        url= self.make_request_url("/search?&page=")
        self.get_page_listings(url)

    

      

    def get_page_listings(self, page_url):
        page_num = 1
        while page_num<=3:
            
            
            current_page_url = f"{page_url}{page_num}"

            page_content = self.service.make_get_request(current_page_url)
            if not page_content:
                break
            

            soup = BeautifulSoup(page_content, "html.parser")
            new_links_found = False

            # Get featured article links
            banner_article_links = soup.find_all("div", class_="big-feature col-md-12")
            if banner_article_links:   
                anchors = []
                for item in banner_article_links:
                    anchors.extend(item.find_all("a"))
                href_links = [a['href'] for a in anchors if 'href' in a.attrs]
                for link in href_links:
                    if self.is_valid_article_link(link):
                        self.unique_links.add(link)
                        new_links_found = True

            # Get other news links from the category page
            div_tags = soup.find_all('div', class_='items')
            href_links = [div.find('a')['href'] for div in div_tags if div.find('a') and 'href' in div.find('a').attrs]
            for link in href_links:
                if self.is_valid_article_link(link):
                    self.unique_links.add(link)
                    new_links_found = True

            # Process each new link
            if new_links_found:
                for link in self.unique_links:
                    self.get_page_details(link)

            page_num += 1


    def is_valid_article_link(self, link):
        # Exclude links that contain 'photo-detail' or 'author'
        if "photo-detail" in link or "author" in link:
            return False
        # Ensure the link ends with digits
        return bool(re.search(r'\d+$', link))


        

    def get_page_details(self, url):
        page_content = self.service.make_get_request(url)
        if not page_content:
            return
        
        self.service.log.info(f"\nArticle url {url}")
        soup = BeautifulSoup(page_content, "html.parser")

        # Extract title
        title_container = soup.find("h1", class_="news-big-title")
        news_title = title_container.get_text(strip=True) if title_container else "N/A"

        # Extract author (defaulting to "N/A" if not found)
        author = "N/A"
        media_body = soup.find("div", class_="media-body")
        if media_body:
            author_container = media_body.find("h2", class_="main-title")
            if author_container:
                author = author_container.get_text(strip=True)

        # Extract content paragraphs
        content_text = []
        content_body = soup.find("div", class_="editor-box")
        if content_body:
            content_container = content_body.find_all("p")
            for paragraph in content_container:
                content_text.append(paragraph.get_text(strip=True))
        full_content = " ".join(content_text)

        # Extract published date and time   
        article_datetime = None
        published_date_str = "na"
        date_time_container = soup.find("div", class_="published-date col-md-6")
        if date_time_container:
            date_time_text = date_time_container.text.strip()
            if date_time_text:
                cleaned_text = date_time_text.replace('\xa0', ' ')
                date_match = re.search(r',\s*([^,]+ \d{1,2}, \d{4})', cleaned_text)
                time_match = re.search(r'(\d{1,2}:\d{2})', cleaned_text)
                if date_match and time_match:
                    date_t = date_match.group(1)
                    time_t = time_match.group(1)
                    time_t = self.service.convert_nepali_to_english(time_t)

                    try:
                        np_month_str, np_day_str, np_year_str = date_t.split()
                        np_day_str = np_day_str.strip(',')
                    except ValueError:
                        self.service.log.error(f"Unexpected date format: {date_t}")
                    else:
                        try:
                            np_day = int(self.service.convert_nepali_to_english(np_day_str))
                            np_year = int(self.service.convert_nepali_to_english(np_year_str))
                        except ValueError:
                            self.service.log.error(f"Error converting day/year: {np_day_str}, {np_year_str}")
                        else:
                            nepali_months = {
                                "बैशाख": 1, "जेष्ठ": 2, "अषाढ": 3, "श्रावण": 4,
                                "भदौ": 5, "असोज": 6, "कार्तिक": 7, "मंसिर": 8,
                                "पुस": 9, "माघ": 10, "फागुन": 11, "चैत्र": 12
                            }
                            np_month = nepali_months.get(np_month_str)
                            if np_month is None:
                                self.service.log.error(f"Invalid Nepali month encountered: {np_month_str}")
                            else:
                                try:
                                    en_year, en_month, en_day = converter.nepali_to_english(np_year, np_month, np_day)
                                except Exception as e:
                                    self.service.log.error(f"Date conversion error for {date_t}: {e}")
                                else:
                                    try:
                                        article_hour, article_minute = map(int, time_t.split(":"))
                                    except ValueError:
                                        self.service.log.error(f"Invalid time format: {time_t}")
                                    else:
                                        article_datetime = datetime(en_year, en_month, en_day, article_hour, article_minute)
                                        published_date_str = article_datetime.strftime("%Y-%m-%d %H:%M:%S")
                                        
                                        # Filter out articles older than the threshold (e.g., 5 hours)
                                        now = datetime.now()
                                        time_diff = now - article_datetime
                                        threshold_value = 1
                                        if time_diff > timedelta(days=threshold_value):
                                            self.service.log.info(f"Article is older than {threshold_value} days; skipping.")
                                            return
                else:
                    self.service.log.error("Could not extract date or time from the text.")
            else:
                self.service.log.error("Date and time text is empty.")
        else:
            self.service.log.error("Date and time container not found.")

        #to get categry
        match = re.search(r"https?://www\.setopati\.com/([^/]+)/", url)
        if match:
            category= match.group(1)
        else:
            category= None


        news_data = {
            "url": url,
            "category": category,
            "title": news_title,
            "published_date_time": published_date_str,
            "author": author,
            "content": full_content,
        }

        self.service.save_json(news_data,news_title,"setopati")


        