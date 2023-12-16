import requests
import json
import os

if not os.path.exists("nownews"):
    os.mkdir("nownews")

url = "https://www.nownews.com/nn-client/api/v1/cat/entertainment/?pid=6322854"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)

data = json.loads(res.text)

# with open("sample.json", "r", encoding="utf-8") as f:
#     json.load(f)

print(type(res.text))
print(type(data))
print(type(res.json()))

news_list = res.json()["data"]["newsList"]
for news in news_list:
    img_url = news["imageUrl"]
    img_name = img_url.split("?")[0].split("/")[-1]
    img_path = f"nownews/{img_name}"
    res_img = requests.get(img_url, headers=headers)
    with open(img_path, "wb") as f:
        f.write(res_img.content)
    # print(news)
