import requests
from bs4 import BeautifulSoup
import re

from urllib.parse import urlparse

class SS:

    def __init__(self):
        self.base_url =  "https://www.ekantipur.com"

    def get(self):
        url =  self.base_url  + "/"
        res = requests.get(url)
        unique_category_links=set()

        soup =  BeautifulSoup(res.content  , 'html.parser')

        nav_links =soup.find("div",class_="ek-menu-navbar")
        a_tags=nav_links.find_all("a")
        for a_tag in a_tags:
            href = a_tag.get("href")
            if href:
                parsed_url = urlparse(href)
                category = parsed_url.path.strip("/").split("/")[0]  # Extract category name
                unique_category_links.add(category)
                print(category)



        # breakpoint()


if __name__ == "__main__":
    SS().get()


from datetime import datetime, timedelta
from urllib.parse import urlparse

def get_page_category(self):
    # Fetch and parse the homepage
    soup = self.get_soup(self.base_url)  # Assuming get_soup fetches and parses the page
    nav_links = soup.find("div", class_="ek-menu-navbar")
    
    if not nav_links:
        self.service.log.error("Failed to find navigation links")
        return
    
    a_tags = nav_links.find_all("a")
    unique_categories = set()

    for a_tag in a_tags:
        href = a_tag.get("href")
        if href:
            parsed_url = urlparse(href)
            category = parsed_url.path.strip("/").split("/")[0]  # Extract category name
            unique_categories.add(category)

    self.service.log.info(f"Found categories: {unique_categories}")

    # Iterate over days and categories
    for i in range(self.threshold_days):
        target_date = datetime.now() - timedelta(days=i)
        date_str = target_date.strftime("%Y/%m/%d")

        for category in unique_categories:
            listing_url = f"{self.base_url}/{category}/{date_str}"
            self.service.log.info(f"Scraping category '{category}' for date {date_str}: {listing_url}")
            self.get_page_listings(listing_url, category)
