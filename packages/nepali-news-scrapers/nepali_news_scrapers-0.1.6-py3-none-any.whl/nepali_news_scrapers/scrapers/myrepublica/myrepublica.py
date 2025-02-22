import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
import json
import re
import os
from services.scraper_service import ScraperService


class MyRepublicaScraper:
    def __init__(self,scraper_service:ScraperService):
        self.base_url = "https://myrepublica.nagariknetwork.com/"
        self.service = scraper_service
        self.listed_urls = set()  # To avoid processing duplicate URLs
        
       

    def make_request_url(self, url):
        return self.base_url.strip().rstrip("/") + "/" + url.strip().lstrip("/")
        

    def start(self):
        self.get_page_category()

        
    
    def get_page_category(self):
        categories = ["economy","politics","society","world","op-ed","sports","republica-watch","diaspora","market"]
        for category in categories:
            try:
                self.service.log.info(f"Starting scraping for category: {category}")
                self.get_page_listing(category)
            except Exception as e:
                self.service.log.error(f"Failed to scrape category {category}: {e}")
                continue
        

            


    def get_page_listing(self, category):
        page = 1
        continue_scraping = True

        while continue_scraping:
            if page >3:
                break

            


            relative_url = f"category/{category}?page={page}"
            page_list_api_endpoint = self.make_request_url(relative_url)
            #passing url to get articles in the featured section
            self.get_featured_sections(page_list_api_endpoint)

            self.service.log.info(f"Fetching page {page} from: {page_list_api_endpoint}")



            page_content = self.service.make_get_request(page_list_api_endpoint)
            if not page_content:
                break

            soup = BeautifulSoup(page_content, "html.parser")

            # Find all <a> tags with href that include "/news/"
            listings = soup.find_all("a", href=re.compile("/news/"))

            if not listings:
                self.service.log.info(f"No more listings found for category '{category}'. Ending scraping for this category.")
                break 

            for listing in listings:
                news_url = listing.get("href")
                full_news_url = (
                    news_url
                    if news_url.startswith("http")
                    else self.make_request_url(news_url)
                )
                # print("Newsurlhere",news_url)


                # Avoid processing duplicate URLs
                if full_news_url in self.listed_urls:
                    continue
                self.listed_urls.add(full_news_url)


                # Extract title from the listing
                title_elem = listing.find("h3", class_=re.compile("rep-title"))
                title = title_elem.get_text(strip=True) if title_elem else "No Title"
                self.service.log.info(f"Found news: {title}")
                self.service.log.info(f"URL: {full_news_url}")

                # Optionally, extract news ID from the URL (if present)
                news_id_match = re.search(r'-(\d+-\d+)\.html', full_news_url)
                news_id = news_id_match.group(1) if news_id_match else None
                if news_id:
                    self.service.log.info(f"News ID: {news_id}")

                # Fetch and process the details page

                self.get_page_details(full_news_url)

                self.service.log.info("-" * 40)

            page += 1
            time.sleep(1)  # Respectful delay between pages


    def get_featured_sections(self, url):
        self.service.log.info(f"Extracting featured sections from: {url}")
        page_content = self.service.make_get_request(url)
        if not page_content:
            return
        

        soup = BeautifulSoup(page_content, "html.parser")

        # Find the container div with the specified class
        container_div = soup.find("div", class_="col-span-1 lg:col-span-9")
        if not container_div:
            self.service.log.warning("Featured section container not found.")
            return

        # Extract links within the container
        featured_section_links = container_div.find_all("a", href=True)
        urls = [tag['href'] for tag in featured_section_links if tag['href'].startswith("https://myrepublica.nagariknetwork.com/")]

        # breakpoint()
        for extracted_url in urls:
            self.service.log.info(f"Extracted URL from featured section: {extracted_url}")
            self.get_page_details(extracted_url)




    def get_page_details(self, url):
       
        headers = {
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.7",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Sec-GPC": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Brave\";v=\"133\", \"Chromium\";v=\"133\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
                }
        
        self.service.log.info(f"Fetching details for: {url}")
        page_content = self.service.make_get_request(url,headers=headers)

        if not page_content:
            return
        
        page_text = page_content.decode('utf-8')


        soup = BeautifulSoup(page_text, "html.parser")

            # Extract the news title
        news_title_elem = soup.find("h1", {"class": "rep-headline--large"})
        if news_title_elem:
            news_title = news_title_elem.get_text(strip=True)
        else:
            self.service.log.error("News title not found.")
            return

            # Extract category 
        category_elems = soup.find_all("span", {"class": "rep-body--small--sans"})
        category_text = category_elems[2].get_text(strip=True) if len(category_elems) >= 3 else "No Category"

            # Extract author 
        author = "No Author"
        by_span = soup.find("span", {"class": "underline"})
        if by_span:
            a_elem = by_span.find("a")
            if a_elem:
                author = a_elem.get_text(strip=True)

            # Extract publication date/time using regex search (if content is rendered via JS)
        time_date_match = re.search(r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})", page_text)
        if time_date_match:
            time_date_str = time_date_match.group(1)
            try:
                publish_datetime = datetime.strptime(time_date_str, "%Y-%m-%dT%H:%M:%S")
                publish_date = publish_datetime.strftime("%Y-%m-%d")
                publish_time = publish_datetime.strftime("%H:%M:%S")
            except Exception as e:
                self.service.log.error(f"Error parsing date/time: {e}")
                publish_date = publish_time = "Unknown"
        else:
            publish_date = publish_time = "Unknown"

            # Filter out news based on the publication date and time.
        if publish_date != "Unknown" and publish_time != "Unknown":
            published_datetime_str = f"{publish_date}T{publish_time}"
            try:
                published_datetime = datetime.strptime(published_datetime_str, "%Y-%m-%dT%H:%M:%S")
                    
                    #time filter
                if datetime.now() - published_datetime > timedelta(hours=24):
                    self.service.log.info(f"Skipping news published on {published_datetime}")
                    return
            except Exception as e:
                self.service.log.error(f"Error during datetime comparison: {e}")

            # Extract image (if available)
        image_elem = soup.find("img", {"class": "rep-image--full"})
        image_url = image_elem.get("src") if image_elem else "No Image"
        if image_url:
            self.service.log.info(f"Found image: {image_url}")

            # Extract tags (if available)
        tags = []
        tag_elems = soup.find_all("span", {"class": "rep-misc__tag"})
        for tag_elem in tag_elems:
            tag_text = tag_elem.get_text(strip=True)
            if tag_text:
                tags.append(tag_text)

            # Extract content
        content_div = soup.find("div", {"id": "content"})
        para_text = []
        if content_div:
            paragraphs = content_div.find_all("p")
            para_text = [p.get_text(strip=True) for p in paragraphs]
        else:
            self.service.log.error("Content not found.")

        
        news_data = {
                "url": url,
                "title": news_title,
                "category": category_text,
                "author": author,
                "published_time": publish_time,
                "published_date": publish_date,
                "content": para_text,
            }

        self.service.save_json(news_data,news_title,"myrepublica")
        