from abc import ABC, abstractmethod
# from scrapers import scrapers
import os
import re
import json
import time
import logging
import requests

class Scraper(ABC):
    """Interface to be implimented by every scrapers
    every scrapers should have the start() and get_details() methods
    """

    @abstractmethod
    def start(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_details(self, url: str, *args, **kwargs):
        pass


class ScraperService:
    """Scraper Service class to have all the common functionalities needed for scraping task"""
    
    def __init__(self,json_dir):
        self.json_dir = json_dir
        os.makedirs(self.json_dir, exist_ok=True)

        logging.basicConfig(level=logging.INFO)

        
        self.log = logging.getLogger(__name__)

    
    #function that makes an http get requesstand returns the res.content 
    def make_get_request(self, url,headers=None):
        try:
            response = requests.get(url,headers=headers,timeout=10)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            self.log.error(f"Error making request to {url}: {str(e)}")
            return None
    
    def make_post_request(self,url,data=None,headers=None):
        try:
            response = requests.post(url, data=data, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.log.error(f"Error making POST request to {url}: {str(e)}")
            return None

    def save_json(self,data,title,filename_prefix):
    
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        title_slug = re.sub(r"\W+", "_", title)[:10]  
        filename = os.path.join(self.json_dir, f"{filename_prefix}_{title_slug}_{timestamp}.json")
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            self.log.info(f"Saved data to {filename}")
        except Exception as e:
            self.log.error(f"Error saving to JSON: {e}")
    
    @staticmethod
    def convert_nepali_to_english(nepali_number):
        nepali_digits = "०१२३४५६७८९"
        english_digits = "0123456789"
        translation_table = str.maketrans(nepali_digits, english_digits)
        return nepali_number.translate(translation_table)





class ScraperRunner:
    @classmethod
    def get_scraper_instance(cls, scraper_name):
        from scrapers import scrapers 
        
        scraper_class = scrapers.get(scraper_name)
        if scraper_class:
            scraper_service = ScraperService(json_dir="JSONS")
            return scraper_class(scraper_service)  # Create an instance properly
        else:
            raise ValueError(f"Scraper {scraper_name} not found")
