import os
import json
import time
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

from services.scraper_service import Scraper, ScraperService


class NepaliTimesScraper(Scraper):
    def __init__(self, scraper_service: ScraperService):
        self.service = scraper_service
        self.graphql_url = "https://nepalitimes-hasura.superdesk.org/v1/graphql"
        self.base_url = "https://nepalitimes.com"

        self.categories = {
            "news": 8,
            "multimedia": 40,
            "here-now": 41,  # features
            "editorial": 43,
            "opinion": 12,
            "opinion/missmotivation": 65,
            "opinion/angrezi": 71,
            "iwitness": 69,
            "review": 11,
            "business": 9,
            "margins": 68,
        }
        

    def make_request_url(self, url: str) -> str:
        return self.base_url.strip().rstrip("/") + "/" + url.strip().lstrip("/")

    def start(self):
        try:
            for category, route_id in self.categories.items():
                self.service.log.info(f"Scraping Category: {category}")
                self.get_articles(category, route_id)
        except Exception as e:
            self.service.log.error(f"Error scraping Nepali Times: {str(e)}")

    def get_articles(self, category: str, route_id: int):
        payload = {
            "query": """
            query getArticles($routeId: Int) {
                items: swp_article(offset: 0, limit: 50, order_by: {published_at: desc}, where: {route_id: {_eq: $routeId}}) {
                    id
                    title
                    published_at
                    slug
                    swp_route { staticprefix }
                }
            }
            """,
            "variables": {"routeId": route_id},
        }
        headers = {
            "accept": "*/*",
            "content-type": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/133.0.0.0 Safari/537.36",
        }

        response = self.service.make_post_request(
            self.graphql_url, data=json.dumps(payload), headers=headers
        )
        if not response:
            self.service.log.error(f"GraphQL request failed for category '{category}'")
            return

        articles = response.get("data", {}).get("items", [])
        self.service.log.info(f"Fetched {len(articles)} articles for category '{category}'.")

        for article in articles:
            self.process_article(article, category)

    def process_article(self, article, category: str):
        news_id = article.get("id")
        title = article.get("title")
        published_at_str = article.get("published_at")
        slug = article.get("slug")
        staticprefix = article.get("swp_route", {}).get("staticprefix", "")
        article_link = f"{self.base_url}{staticprefix}/{slug}"

        try:
            published_at_dt = datetime.fromisoformat(published_at_str)
        except Exception as e:
            self.service.log.error(f"Date parsing error for article {news_id}: {e}")
            return
        
        threshold_days = 1
        now = datetime.now()
        if now - published_at_dt >= timedelta(days=threshold_days):
            self.service.log.info(f"Skipping old article: {title}")
            return

        details = self.get_details(article_link)
        if details:
            article_data = {
                "id": news_id,
                "title": title,
                "published_at": published_at_dt.isoformat(),
                "url": article_link,
                "category": category,
                "content": details.get("content", ""),
            }
            self.service.save_json(article_data, title, "NepaliTimes")
        else:
            self.service.log.error(f"Failed to retrieve details for article: {article_link}")

    def get_details(self, url: str, *args, **kwargs):
        response = self.service.make_get_request(url, headers=self.headers)
        if not response:
            self.service.log.error(f"Failed to fetch article content from {url}")
            return None

        try:
            soup = BeautifulSoup(response, "html.parser")
        except Exception as e:
            self.service.log.error(f"Error parsing HTML for {url}: {e}")
            return None

        subheading = soup.find("span", class_="article__subhead")
        article_body = soup.find("div", class_="article__text")
        if not article_body:
            self.service.log.warning(f"Article body not found: {url}")
            return None

        # Remove unwanted elements
        for tag in article_body.find_all(["script", "style", "iframe", "nav", "footer", "aside", "figure"]):
            tag.decompose()

        content = ""
        if subheading:
            content += subheading.get_text(strip=True) + "\n\n"
        content += article_body.get_text("\n", strip=True)

        return {"content": content.strip(), "url": url}


