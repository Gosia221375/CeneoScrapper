import requests
from bs4 import BeautifulSoup

url = "https://www.ceneo.pl/45863470#tab=reviews"

response = requests.get(url)

page_dom = BeautifulSoup(response.text,'html.parser')
print(page_dom.prettify())

opinions = page_dom.select("div.js_product-review")
print(type(opinions))
opinion = opinions.pop()

opinion_id = opinion["data-entry-id"]
author = opinion.select_one("span.user-post_author-name").text.strip()
rcmd = opinion.select_one("span.user-post_author-recommendation > em").text.strip()
score = opinion.select_one("span.user-post_score-count").text.strip()
content = opinion.select_one("div.user-post_text").text.strip()
posted_on = opinion.select_one("span.user-post_published > time:nth-child(1)")["datetime"]
bought_on = opinion.select_one("span.user-post_published > time:nth-child(2)")["datetime"]
useful_for = opinion.select_one("button.vote-yes > span").text.strip()
useless_for = opinion.select_one("button.vote-no > span").text.strip()
pros = opinion.select("div.review-feature_title--positives ~ div.review-feature_item")
pros = [item.text.strip() for item in pros]

print(type(pros))
print(pros)



print(type(author))
print(author)


print(opinion.prettify())