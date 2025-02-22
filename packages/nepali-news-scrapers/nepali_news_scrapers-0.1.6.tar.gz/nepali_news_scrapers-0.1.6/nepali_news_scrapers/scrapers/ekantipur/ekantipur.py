from urllib.parse import urlparse
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from services.scraper_service import ScraperService


class EkantipurScraper:
    def __init__(self, scraper_service: ScraperService):
        self.base_url = "https://ekantipur.com"
        self.unique_links = set()
        self.service = scraper_service
       
        self.threshold_days = 2
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/133.0.0.0 Safari/537.36",
        }

    def make_request_url(self, url):
        return self.base_url.rstrip("/") + "/" + url.lstrip("/")

    def start(self):
        self.get_page_category()

    def get_page_category(self):
        page_content = self.service.make_get_request(self.base_url,self.headers)
        if not page_content:
            return
        
        soup = BeautifulSoup(page_content, "html.parser")  
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

  
    def get_page_listings(self, listing_url, category):
       

        page_content = self.service.make_get_request(listing_url, self.headers)
        if not page_content:
            return

        soup = BeautifulSoup(page_content, "html.parser")
        articles = soup.find_all("article", class_="normal")
        
        for article in articles:
            a_tags = article.find_all("a")
            for a in a_tags:
                href = a.get("href")
                if href and "author" not in href:
                    full_url = self.make_request_url(href)
                    if full_url not in self.unique_links:
                        self.unique_links.add(full_url)
                        self.get_details(full_url)

    def get_details(self, url):
        self.service.log.info(f"Fetching details for article: {url}")
        page_content = self.service.make_get_request(url)
        if not page_content:
            return

        soup = BeautifulSoup(page_content, "html.parser")

        category_text = soup.find("div", class_="cat_name").text.strip() if soup.find("div", class_="cat_name") else ""
        news_title = "No title found"
        title_h1 = soup.find("h1", class_="eng-text-heading")  # First structure
        if title_h1:
            news_title = title_h1.text.strip()
        else:
            article_header = soup.find("div", class_="article-header")  # Second structure
            if article_header:
                title_h1 = article_header.find("h1")
                if title_h1:
                    news_title = title_h1.text.strip()      
        date_span = soup.find("span", class_="published-at")
        date_part, time_part = (date_span.text.strip().replace("प्रकाशित :", "").strip().rsplit(" ", 1) if date_span else ("", ""))
        
        author_details = [a.text.strip() for a in soup.find_all("h3", class_="author-name")[:2]]
        if not author_details:
            authors_div = soup.find("div", class_="author")
            author_details = [authors_div.text.strip()] if authors_div else []

        sub_heading_div = soup.find("div", class_="sub-heading")
        highlights = "".join([li.text.strip() for li in sub_heading_div.find_all("li")]) if sub_heading_div else ""

        news_block = soup.find("div", class_="current-news-block")

        if news_block:
            # Extract text from <p> tags inside the identified div
            content = "\n".join([p.get_text(strip=True) for p in news_block.find_all("p")])
        else:
            # If the main div is not found, fallback to extracting all <p> tags
            content = "\n".join([p.get_text(strip=True) for p in soup.find_all("p")])

        news_data = {
            "url": url,
            "title": news_title,
            "category": category_text,
            "author": author_details,
            "published_date": date_part,
            "published_time": time_part,
            "content": highlights + "\n" + content
        }

        self.service.save_json(news_data, news_title, "ekantipur")



