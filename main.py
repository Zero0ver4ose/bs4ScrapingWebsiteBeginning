from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_texts = []
article_links = []

article_tags= soup.find_all(name="span", class_="titleline")
for tags in article_tags:
    article_texts.append(tags.getText())
    article_link = tags.select_one(selector="a")
    article_link = article_link.get("href")
    article_links.append(article_link)

#Comprehension
article_upvote = [int(i.getText().split()[0]) for i in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvote)

max_nr = max(article_upvote)
largest_index = article_upvote.index(max_nr)
print(article_texts[largest_index])
print(article_links[largest_index])
