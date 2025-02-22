from bs4 import BeautifulSoup
import requests

class NepseAlphaScraper:

    def __init__(self):
        pass

    def get_page_details(self):
        # Path to your local HTML file
        # file_path = "C:/Users/Asus/Downloads/kalika.html"

        # Open and read the local HTML file
        # with open(file_path, "r", encoding="utf-8") as file:
        #     res_html = file.read()

        url="https://nepsealpha.com/post/detail/6408/today-is-the-last-day-to-secure-siddharth-premier-insurances-dividend"

        res_html = requests.get(url)
        print(res_html.status_code)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(res_html.content, "html.parser")

        # Extract news title
        news_title_container = soup.find("h2", {"class": "post_title"})
        if news_title_container:
            news_title=news_title_container.text.strip()
        else:
            news_title = "N/A"

        
        #extract datetime
        date_container = soup.find("li", {"class": "detail date"})
        if date_container:
            date_time = date_container.text.strip()
        else:
            date_time = "N/A"

        #extract the author
        author_container = soup.find("li", {"class": "detail author"})
        if author_container:
            author = author_container.text.strip()
            author=author.lstrip("By").strip()
        else:
            author = "N/A"

        #extract the contents
        content_container = soup.find("div", {"class": "text"})
        if content_container:
            contents = content_container.text.strip()
        else:
            contents = "N/A"
            

        # Example breakpoint for debugging
        breakpoint()

if __name__ == "__main__":
    NepseAlphaScraper().get_page_details()
