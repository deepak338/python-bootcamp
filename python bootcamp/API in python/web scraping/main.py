from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/news")
yc_web_page=response.text

soup=BeautifulSoup(yc_web_page,'html.parser')

articles=soup.find_all(name='span',class_='titleline')
article_text=[]
article_links=[]
for article_tag in articles:
    text = article_tag.get_text()
    article_text.append(text)
    link = article_tag.a.get('href') if article_tag.a else None
    article_links.append(link)


article_upvotes = [int(score.get_text().replace(" points", "")) for score in soup.find_all(name='span', class_='score')]
articles = zip(article_text, article_links, article_upvotes)

highest_voted_article = max(articles, key=lambda x: x[2]) if article_upvotes else None
if highest_voted_article:
    article_name, article_link, article_upvote = highest_voted_article
    print("Name of highest voted article:", article_name)
    print("Link of highest voted article:", article_link)
else:
    print("No articles found.")



# print(article_text)
# print(article_links)
# print(article_upvote)


