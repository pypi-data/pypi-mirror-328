import re
import json
import time
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from services.scraper_service import ScraperService


class MeroLaganiScraper:
    def __init__(self, scraper_service: ScraperService):
        self.base_urls = {
            "NP": "http://merolagani.com/",
            "ENG": "http://eng.merolagani.com/",
        }
        self.service = scraper_service

    def make_request_url(self, url, lang):
        base_url = self.base_urls.get(lang, self.base_urls["NP"])
        return base_url.rstrip("/") + "/" + url.lstrip("/")

    def start(self):
        for lang in ["NP", "ENG"]:
            self.get_page_listing(lang)

    def get_page_listing(self, lang):
        page_num = 1
        continue_scraping = True

        while continue_scraping:
            url = f"/handlers/webrequesthandler.ashx?type=get_news&newsID=0&newsCategoryID=0&symbol=&page={page_num}&pageSize=16&popular=false&includeFeatured=true&news=%23ctl00_ContentPlaceHolder1_txtNews&languageType={lang}"
            page_list_api_endpoint = self.make_request_url(url, lang)

            news_list = self.service.make_get_request(page_list_api_endpoint)

            if not news_list:
                self.service.log.warning(f"Failed to fetch news list from {page_list_api_endpoint}")
                break

            try:
                news_list = json.loads(news_list)
            except json.JSONDecodeError:
                self.service.log.error(f"Invalid JSON response from {page_list_api_endpoint}")
                break

            for news_item in news_list:
                news_id = news_item.get("newsID")
                news_date_str = news_item.get("newsDateAD")

                if not news_id or not news_date_str:
                    self.service.log.warning(f"Skipping news due to missing data: {news_item}")
                    continue

                date_obj = datetime.strptime(news_date_str, "%Y-%m-%dT%H:%M:%S.%f")
                if datetime.now() - date_obj >= timedelta(days=1):
                    continue_scraping = False
                    break

                details_page_url = self.make_request_url(f"/NewsDetail.aspx?newsID={news_id}", lang)
                self.get_page_details(news_id, details_page_url, lang)

            page_num += 1

    def get_page_details(self, news_id, url, lang):
        page_content = self.service.make_get_request(url)
        if not page_content:
            self.service.log.error(f"Failed to fetch news details for {news_id}")
            return

        soup = BeautifulSoup(page_content, "html.parser")

        news_title = soup.find("h4", {"id": "ctl00_ContentPlaceHolder1_newsTitle"})
        news_title = news_title.get_text(strip=True) if news_title else "Not found"

        time_date_container = soup.find("span", {"id": "ctl00_ContentPlaceHolder1_newsDate"})
        publish_date, publish_time = "none", "none"
        if time_date_container:
            time_date = time_date_container.text.strip()
            match = re.match(r'([A-Za-z]+ \d{1,2}, \d{4}) (\d{1,2}:\d{2} [APM]+)', time_date)
            if match:
                publish_date, publish_time = match.group(1), match.group(2)

        news_source = soup.find("span", {"id": "ctl00_ContentPlaceHolder1_newsSource"})
        news_source = news_source.text.strip() if news_source else "Not found"

        news_overview = soup.find("div", {"id": "ctl00_ContentPlaceHolder1_newsOverview"})
        news_overview = news_overview.text.strip() if news_overview else ""

        content_container = soup.find("div", {"id": "ctl00_ContentPlaceHolder1_newsDetail"})
        content = content_container.text.strip() if content_container else "No content found"

        category_container = soup.find("ul", class_="breadcrumb")
        category = category_container.find_all("li")[-1].text.strip() if category_container else "Uncategorized"

        news_data = {
            "url": url,
            "title": news_title,
            "category": category,
            "author": news_source,
            "published_time": publish_time,
            "published_date": publish_date,
            "content": news_overview + " " + content
        }

        self.service.save_json(news_data, news_title, "merolagani")
        self.service.log.info(f"Saved news: {news_title} ({lang})")


# Usage:
# scraper_service = ScraperService()
# MeroLaganiScraper(scraper_service).start()
