import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime, timedelta
import re
from nepali.date_converter import converter
from services.scraper_service import ScraperService



class GorkhaPatraScraper:
    def __init__(self,scraper_service:ScraperService):
        self.base_url = "https://gorkhapatraonline.com"
        self.unique_links = set()
        self.service = scraper_service

    def make_request_url(self, url):
        return self.base_url.strip().rstrip("/") + "/" + url.strip().lstrip("/")

    def start(self):
        self.get_page_category()


    def get_page_category(self):
        categories = ["","national",
            "entertainment",
            "economy",
            "editorial",
            "new-nepal",
            "health",
            "international",
            "culture",
            "corporate",
            "loksewa",
            "bank",
            "culture-and-arts",
            "diaspora",
            "share",
            "thoughts",
            "news-today",
            "open",
            "politics",
            "sports",
            "cricket",
            "tourism",
            "earthquake",
            "interesting-context",
            "education",
            "football",
            "video-gallery",
            "interview",
            "saturday",
            "photo-feature",
            "crime",
            "technology",
            "koshi",
            "province",
            "province-two",
            "province-three",
            "province-four",
            "province-five",
            "province-six",
            "province-seven",
        ]

        for category in categories:
            if category == "":
                page_url = self.make_request_url(f"{category}")
            else:
                page_url = self.make_request_url(f"categories/{category}")
            self.get_page_listings(page_url, category)

    def get_page_listings(self, page_url, category):
        page_num = 1

        while page_num<=2:
            
            current_page_url = f"{page_url}?page={page_num}"
            self.service.log.info(f"Scraping Category {category} and Page: {current_page_url}")

            page_content = self.service.make_get_request(current_page_url)
            if not page_content:
                break

            soup = BeautifulSoup(page_content, "html.parser")
            title_elements = soup.find_all(
                ["h2", "h3", "h4", "h1"], class_="item-title"
            )

            new_links_found = False
            for title in title_elements:
                a_tag = title.find("a")
                if a_tag and a_tag.get("href"):
                    full_link = a_tag["href"]
                    if full_link not in self.unique_links:
                        self.unique_links.add(full_link)
                        self.get_page_details(full_link, category)
                        new_links_found = True

            if not new_links_found:
                break
            page_num += 1

    def get_page_details(self, url, category):
        page_content = self.service.make_get_request(url)
        if not page_content:
            return

        self.service.log.info(f"\nArticle url {url}")

        soup = BeautifulSoup(page_content, "html.parser")

        # Extract title
        title_container = soup.find(
            "h1", {"class": "single-top-title mb-3 sticky-title"}
        )
        news_title = title_container.text.strip() if title_container else "N/A"

        # Extract author
        author_container = soup.find("div", {"class": "blog-author"})
        author = (
            author_container.text.strip().lstrip("By").strip()
            if author_container
            else "N/A"
        )

        # Extract datetime
        date_container = soup.find("span", {"class": "mr-3 font-size-16"})
        date_inside = date_container.text.strip() if date_container else ""
        # self.service.log.info(f"Extracted Date-Time: {date_inside}")

        actual_time = None
        published_time_container = soup.find_all("span", {"class": "mr-3 font-size-16"})

    
        if len(published_time_container) >= 2:
            published_time = published_time_container[1].text.strip()
            time_match_re = re.search(
                r"(\d+)\s*(सेकेण्ड|मिनेट|घण्टा|दिन|हप्ता|महिना|वर्ष)\s+पहिले", published_time
            )

            if time_match_re:
                nepali_amount = time_match_re.group(1)
                unit = time_match_re.group(2)
                english_amount = int(self.service.convert_nepali_to_english(nepali_amount))
                current_time = datetime.now()

                delta = None
                if unit == "सेकेण्ड":
                    delta = timedelta(seconds=english_amount)
                elif unit == "मिनेट":
                    delta = timedelta(minutes=english_amount)
                elif unit == "घण्टा":
                    delta = timedelta(hours=english_amount)
                elif unit == "दिन":
                    delta = timedelta(days=english_amount)
                elif unit == "हप्ता":
                    delta = timedelta(weeks=english_amount)
                elif unit == "महिना":
                    delta = timedelta(days=30 * english_amount)
                elif unit == "वर्ष":
                    delta = timedelta(days=365 * english_amount)

                if delta:
                    actual_time = current_time - delta
                    # self.service.log.info(f"Computed actual_time from relative: {actual_time}")

        # Process static date if actual_time not set
            if actual_time is None and date_inside:
                try:
                    date_part, day_part = date_inside.split(",", 1)
                    date_part = date_part.strip()


                    np_day_str, np_month_str, np_year_str = date_part.split()
                    np_day = int(self.service.convert_nepali_to_english(np_day_str))
                    nepali_months = {
                        "बैशाख": 1,
                        "जेष्ठ": 2,
                        "अषाढ": 3,
                        "श्रावण": 4,
                        "भदौ": 5,
                        "असोज": 6,
                        "कार्तिक": 7,
                        "मंसिर": 8,
                        "पुष": 9,
                        "माघ": 10,
                        "फागुन": 11,
                        "चैत्र": 12,
                    }
                    np_month = nepali_months.get(np_month_str)
                    np_year = int(self.service.convert_nepali_to_english(np_year_str))

                    en_year, en_month, en_day = converter.nepali_to_english(
                        np_year, np_month, np_day
                    )
                    actual_time = datetime(en_year, en_month, en_day)
                    self.service.log.info(f"Computed actual_time from static date: {actual_time}")
                except Exception as e:
                    self.service.log.error(f"Error parsing static date: {e}")
                    actual_time = datetime.now()

            # Fallback to current time if all parsing failed
            if actual_time is None:
                actual_time = datetime.now()
                self.service.log.warning("Using current time as fallback for article datetime")

            current_datetime = datetime.now()
            time_difference = current_datetime - actual_time

            if time_difference > timedelta(days=1):
                self.service.log.info(f"Skipping article {url} older than 1 day: {actual_time}")
                return


        # Extract content
        content_container = soup.find_all("div", {"class": "blog-details"})
        if content_container:
            para_container = content_container[3]
            para_text_container = para_container.text.strip()
            contents_str = (
                para_text_container.replace("\t", "")
                .replace("\n", "")
                .replace("                            ", "")
                if para_text_container
                else "N/a"
            )
        else:

            contents_str = "N/A"  # incase the elements are not found

        news_data = {
            "url": url,
            "category": category,
            "title": news_title,
            "published_date_time": actual_time.strftime("%Y-%m-%d %H:%M:%S"),
            "author": author,
            "content": contents_str,
        }

        self.service.save_json(news_data,news_title,"gorkhapatra")
