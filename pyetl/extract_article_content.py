import requests
from bs4 import BeautifulSoup

article_url = "https://www.ptt.cc/bbs/joke/M.1700839968.A.2D4.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

res = requests.get(article_url, headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

article_content_tag = soup.select_one("#main-content")

# <div class="article-metaline"><span class="article-meta-tag">作者</span>
# print(article_content_tag)

article_content_tag.select_one("div").extract()
print(article_content_tag)
