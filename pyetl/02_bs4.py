import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/joke/index.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

res = requests.get(url=url, headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

# print(soup)

logo_list = soup.findAll("a", {"id": "logo"})
logo_list = soup.find_all("a", {"id": "logo"})
print(logo_list)
print(logo_list[0])
print(logo_list[0].text)

logo = soup.find("a", {"id": "logo"})
print(logo)
print(logo.text)
print("https://www.ptt.cc" + logo["href"])

logo = soup.find("a", id="logo")
print(logo)
print(logo.text)
print("https://www.ptt.cc" + logo["href"])

title_tag_list = soup.select("div.title")
print(title_tag_list[0])
title = title_tag_list[0].find("a")
print(title.text)
print("https://www.ptt.cc" + title["href"])
