import requests
import random
import requests
from bs4 import BeautifulSoup
import re
import json
import time
from datetime import datetime, timedelta
import os
from services.scraper_service import ScraperService



class ShareSansarScraper:

   
    def __init__(self,scraper_service:ScraperService):
        # Base URLs for different languages
        self.base_url="https://www.sharesansar.com/"
        self.service = scraper_service

    def make_request_url(self, url):
        return self.base_url.strip().rstrip("/") + "/" + url.strip().lstrip("/")

    def start(self):
            self.get_page_category()

    def get_page_category(self):
        categories=["exclusive","dividend-right-bonus","latest","interview","ipo-fpo-news","share-listed","expert-speak","mutual-fund","weekly-analysis","company-analysis"]

        for category in categories:
            url = f"category/{category}"
            self.service.log.info(f"Current Cateogory: {category}")

            page_url = self.make_request_url(url)
            self.get_page_listings(page_url)

    def get_page_listings(self, page_url, depth=2): #depth = number of pages to retrieve
        current_depth = 0  # Track how many pages we have scraped

        while current_depth < depth:
            page_content = self.service.make_get_request(page_url)
            if not page_content:
                break
            

            # Parse the current page source
            soup = BeautifulSoup(page_content, "html.parser")

            # Find all news containers
            containers = soup.find_all("div", class_="featured-news-list margin-bottom-15")

            unique_links = set()

            # Regex pattern to extract only <a> links
            pattern = r'<a\s+[^>]*href="(https?://[^"]*newsdetail[^"]*)"'  

            # Loop through each container
            for container in containers:
                container_html = str(container)  # Convert div content to string for regex search
                links = re.findall(pattern, container_html)
                unique_links.update(links)  # Avoid duplicates

            # Process each unique link
            for link in unique_links:
                self.get_page_details(link)
            

            # Check for pagination and get the next page URL
            pagination = soup.find('ul', class_='pagination')
            next_url = None

            if pagination:
                for li in pagination.find_all('li', class_='page-item'):
                    a_tag = li.find('a', class_='page-link')
                    if a_tag and 'next' in a_tag.get('rel', []):  # Look for rel="next"
                        next_url = a_tag['href']
                        break  # Get the first "Next" page URL
            if next_url:
                next_page_url = (page_url+next_url)  # Update page_url to the next page
                current_depth += 1  # Increment the page counter
                self.service.log.info(f"Moving to next page: {next_page_url}")
                page_url = next_page_url
            else:
                self.service.log.info("No more pages to scrape.")
                break  # Exit the loop if no next page is found




    def get_page_details(self,url):   
        page_content = self.service.make_get_request(url)
        if not page_content:
            return

        soup = BeautifulSoup(page_content, "html.parser")
        
        page_title = soup.title.text.strip() 
        # print("Page Title:", page_title)

        news_container = soup.find("div", class_="detail")
        if news_container:
            header = news_container.find("h1")
            if header:
                news_title = header.text.strip() 
            else:
                news_title= None
        
       


        # print("News Title:", news_title)

        date_time_container = soup.find("h5")
        if date_time_container:
            date_text = date_time_container.text.strip()
            date_match = re.search(r"([A-Za-z]{3},\s[A-Za-z]{3}\s\d{1,2},\s\d{4}\s\d{1,2}:\d{2}\s[APM]{2})", date_text)
            # print(date_match)

            if date_match:
                extracted_date_time = date_match.group()  # "Thu, Feb 6, 2025 8:10 AM"
                # print("Full Date and Time:", extracted_date_time)

                # Split date and time
                date_time_parts = extracted_date_time.split(" ")
                publish_date = " ".join(date_time_parts[:4])  
                publish_time = " ".join(date_time_parts[4:])  

                # print("Extracted Date:", publish_date)
                # print("Extracted Time:", publish_time)

            #converting to datetime object
                try:
                    date_obj= datetime.strptime(extracted_date_time,"%a, %b %d, %Y %I:%M %p")
                    date_now = datetime.now()
                    
                    threshold=1
                    if date_now - date_obj >=timedelta(days=threshold):
                        self.service.log.info(f"Skipping {url} as it is older than the {threshold} day 1")
                        return False
                except ValueError:
                    return True #scrape if there is error in parsing datime object

            else:
                publish_date = None
                publish_time = None
            
            

        
        #To get category

        category_container = soup.find("h5")
        if category_container:
            anchor_tags= category_container.find_all("a",{"class":"tags"})

            # print(anchor_tags)

            categories=[]  #to store extracted categories

            for anchors in anchor_tags:
                category = anchors.get_text()
                categories.append(category)
                

        
        #to get author
        author_container = soup.find("a",{"class":"pull-right"})

        if author_container:
            author = author_container.text.strip()
            # print(author)
        else:
            author ="Unknown"

            
        # to get content

        content_container = soup.find("div",{"id":"newsdetail-content"})
        if content_container:
            content =content_container.text.strip()
            # print(content)
        else:
            content ="None"
        
        
        news_data={
            "url":url,
            "title":news_title,
            "category":categories,
            "author":author,
            "published_time":publish_time,
            "published_date":publish_date,
            "content":content

        }
        

        self.service.save_json(news_data,news_title,"sharesansar")

