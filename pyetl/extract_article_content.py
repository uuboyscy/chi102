from typing import Literal

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
COOKIES = {"over18": "1"}

def test(a: Literal["a", "b", "c"]):
    print(123)

def extract_article(article_url: str) -> str:
    res = requests.get(article_url, headers=HEADERS, cookies=COOKIES)

    soup = BeautifulSoup(res.text, "html.parser")

    article_content_tag = soup.select_one("#main-content")

    for tag_name in ["div", "span"]:
        for subtag in article_content_tag.select(tag_name):
            subtag.extract()

    return article_content_tag.text


if __name__ == "__main__":
    article_url = "https://www.ptt.cc/bbs/joke/M.1700839968.A.2D4.html"
    print(
        extract_article(article_url=article_url)
    )
