# from datetime import datetime
# import requests
# from bs4 import BeautifulSoup
# import time
# import re
# import json


# class KathmanduPostScraper:

#     def __init__(self):
#         pass

#     def get_page_details(self):
#         url = "https://kathmandupost.com/interviews/2025/02/02/trump-administration-has-good-reason-to-re-evaluate-american-aid"

#         res = requests.get(url)
#         soup = BeautifulSoup(res.content, "html.parser")

#         # Extract category
#         category_text = soup.find("h4", {"class": "title--line__red"})
#         if category_text:
#             anchor_text = category_text.find("a")
#             category=anchor_text.text.strip()

#         print(category)

#         #extract title
#         news_title =soup.find("title")
#         print(news_title.text.strip())

#         #title_Sub
#         title_sub=soup.find("span",{"class":"title-sub"})
#         if title_sub:
#             print(title_sub.text.strip())
#         else:
#             title_sub=""
        

#         #time and dae
#         date_time_container = soup.find_all("div",{"class":"updated-time"})
#         if date_time_container:
#             date_time=date_time_container[1].text.strip()
#             match = re.search(r'(\w+ \d{1,2}, \d{4}) (\d{2}:\d{2})', date_time)

#             if match:
#                 date_str = match.group(1)
#                 time_str = match.group(2)

#                 datetime_str = f"{date_str} {time_str}"

#                 datetime_object = datetime.strptime(datetime_str, "%B %d, %Y %H:%M")
#                 print("Date and Time:", datetime_object)

    
#                 # Converting to datetime object
        

#         #authr //get anchor tags with attribute/authr

#         author_container = soup.find('a', href=re.compile(r"^/author"))

#         if author_container:
#             text = author_container.text



        
#                 #content
#         content_container = soup.find_all("section", {"class": "story-section"},)
#         if content_container:
#             content = content_container[0].text.strip()


#         breakpoint()
#         # # Generate dynamic JSON filename
#         # timestamp = time.strftime("%Y%m%d-%H%M")
#         # title_slug = re.sub(r"\W+", "_", news_title)[:15]
#         # filename = f"{timestamp}_{title_slug}.json"

#         # # Compile news data
#         # news_data = {
#         #     "url": url,
#         #     "title": news_title,
#         #     "category": category_text,
#         #     "author": authors,
#         #     "published_time": time_part,
#         #     "published_date": date_part,
#         #     "content": highlights + content
#         # }

#         # # Save news data to a JSON file
#         # with open(filename, "w", encoding="utf-8") as f:
#         #     json.dump(news_data, f, ensure_ascii=False, indent=4)


# if __name__ == "__main__":
#     KathmanduPostScraper().get_page_details()

