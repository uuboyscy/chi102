import requests

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
cookies = {"over18": "1"}

res = requests.get(url, headers=headers, cookies=cookies)
# print(res.text)

ss = requests.session()
ss.cookies["over18"] = "1"

res = ss.get(url, headers=headers)
# print(res.text)

print(ss.cookies)