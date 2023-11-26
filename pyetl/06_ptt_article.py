import os

import requests
from bs4 import BeautifulSoup

from extract_article_content import extract_article

folder_name = "ptt_article"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

url = "https://www.ptt.cc/bbs/joke/index.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

for _ in range(5):
    res = requests.get(
        url=url, headers=headers,
    )

    soup = BeautifulSoup(res.text, "html.parser")

    title_tag_list = soup.select("div.title a")
    for title_tag in title_tag_list:
        title = title_tag.text
        article_url = "https://www.ptt.cc" + title_tag["href"]
        # Get article content string
        article_content_string = extract_article(
            article_url=article_url,
        )
        try:
            with open(f"{folder_name}/{title}.txt", "w") as f:
                f.write(article_content_string)
        except FileNotFoundError:
            title = title.replace("/", "-")
            with open(f"{folder_name}/{title}.txt", "w") as f:
                f.write(article_content_string)
        except OSError:
            pass
        except Exception as err:
            print(err)
        print(title)
        print(article_url)

    url = "https://www.ptt.cc" + soup.select("a.btn.wide")[1]["href"]
    print(url)

