import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"
}
url = "https://www.baidu.com"

req = requests.get(url,  headers=headers)

print(req.status_code)
print(req.encoding)
print(req.text)
print(req.content)
