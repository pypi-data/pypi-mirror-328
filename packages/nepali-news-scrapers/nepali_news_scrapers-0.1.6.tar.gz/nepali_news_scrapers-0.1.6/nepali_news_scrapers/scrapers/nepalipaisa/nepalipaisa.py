import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
import json
import re
import os

from services.scraper_service import ScraperService


class NepaliPaisaScraper:
    def __init__(self,scraper_service:ScraperService):
        self.base_url = "https://www.nepalipaisa.com"
        self.service = scraper_service

        

    def make_request_url(self, url):
        return self.base_url.strip().rstrip("/") + "/" + url.strip().lstrip("/")

    def start(self):
        self.get_page_listing()

    def get_page_listing(self):
        page = 1
        continue_scraping = True

        while continue_scraping:
            api_endpoint = "/api/GetNewsList"
            data = {
                "dateType": "",
                "dateFrom": "",
                "dateTo": "",
                "sectors": [],
                "companies": [],
                "categoryId": 0,
                "subCategoryId": 0,
                "pageNo": page,
                "itemsPerPage": 24,
                "pagePerDisplay": 10,
                "newsType": "",
                "sectorGroup": "",
            }

            headers = {
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Language": "en-US,en;q=0.9,fr;q=0.8,ne;q=0.7,pt;q=0.6",
                "Connection": "keep-alive",
                "Content-Type": "application/json; charset=UTF-8",
                "Origin": "https://www.nepalipaisa.com",
                "Referer": "https://www.nepalipaisa.com/news",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
            }

            page_list_api_endpoint = self.make_request_url(api_endpoint)

        

            news_list = self.service.make_post_request(
                page_list_api_endpoint,
                data=json.dumps(data),
                headers=headers
            )

            if not news_list:
                self.service.log.info("Request failed or no content; stopping scraping.")
                break

            

            if not news_list or news_list.get("statusCode") != 200:
                self.service.log.info("No more news or request error. Stopping scraping.")
                break

            result = news_list.get("result")
            if not result:
                self.service.log.info("No 'result' key in the response. Stopping scraping.")
                break

            news_items_group = result.get("data")
            if not news_items_group:
                self.service.log.info("No 'data' key in the result. Stopping scraping.")
                break

            for news_data_item in news_items_group:
                news_date = news_data_item.get("newsDate")
                if news_date:
                    try:
                        date_obj = datetime.strptime(news_date, "%Y-%m-%d")
                        if datetime.now() - date_obj > timedelta(days=1):
                            self.service.log.info(f"Skipping article from {news_date} as it's older than 1 day")
                            return  # or break, based on desired logic
                    except ValueError as e:
                        self.service.log.warning(f"Failed to parse date {news_date}: {e}. Skipping date check.")
                        continue

                news_data_list = news_data_item.get("newsData")
                if news_data_list:
                    for news_item in news_data_list:
                        title = news_item.get("newsTitle")
                        category = news_item.get("category")
                        news_id = news_item.get("newsId")
                        image_url = news_item.get("imageUrl")
                        company_symbols = [company["stockSymbol"] for company in news_item.get("companies", [])]
                        
                        # **Fetching news details**
                        news_details = self.get_page_details(news_id)
                        if news_details:
                            news_data = {
                                "page_url": news_details.get("url"),
                                "news_date": news_date,
                                "title": title,
                                "category": category,
                                "news_id": news_id,
                                "company_symbols": company_symbols,
                                "image_url": image_url,
                                "news_source": news_details.get("news_source"),
                                "content": news_details.get("content"),
                            }
                            # Save extracted data
                            self.service.save_json(news_data, title, "nepalipaisa")
                        else:
                            self.service.log.warning(f"Could not retrieve details for news ID {news_id}")

            page += 1

    def get_page_details(self, news_id):
        """Fetches detailed news content for a given news ID."""
        api_url = self.make_request_url(f"api/GetNews?newsId={news_id}")
        page_url = self.make_request_url(f"news-detail/{news_id}")
        
        # **Using make_request (GET)**
        page_content = self.service.make_get_request(api_url)
        if not page_content:
            self.service.log.error(f"Failed to get content for news ID {news_id}")
            return None

        try:
            data = json.loads(page_content)
        except Exception as e:
            self.service.log.error(f"Error parsing JSON for news ID {news_id}: {e}")
            return None

        result = data.get("result", {})
        news_source = result.get("newsSource", "")
        texts = []
        for desc in result.get("descriptions", []):
            description_html = desc.get("description", "")
            soup = BeautifulSoup(description_html, "html.parser")
            text = soup.get_text(separator="\n", strip=True)
            texts.append(text)
        combined_content = "\n\n".join(texts)
        return {
            "news_source": news_source,
            "content": combined_content,
            "url": page_url
        }


# steps:  inspect -> network -> "Load More" -> check for api -> right click -> copy -> copy as curl

# curl 'https://www.nepalipaisa.com/api/GetNewsList' \
#   -H 'Accept: application/json, text/javascript, */*; q=0.01' \
#   -H 'Accept-Language: en-US,en;q=0.9,fr;q=0.8,ne;q=0.7,pt;q=0.6' \
#   -H 'Connection: keep-alive' \
#   -H 'Content-Type: application/json; charset=UTF-8' \
#   -H 'Origin: https://www.nepalipaisa.com' \
#   -H 'Referer: https://www.nepalipaisa.com/news' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36' \
#   -H 'X-Requested-With: XMLHttpRequest' \

#   --data-raw '{"dateType":"","dateFrom":"","dateTo":"","sectors":[],"companies":[],"categoryId":0,"subCategoryId":0,"pageNo":2,"itemsPerPage":12,"pagePerDisplay":10,"newsType":"","sectorGroup":""}'