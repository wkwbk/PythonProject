import requests

search_content = "spider"
api_url = f"https://api.github.com/search/repositories?q={search_content}"
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69"}

req = requests.get(api_url, headers=ua)
print("状态码：", req.status_code)
req_dic = req.json()
print(req_dic.keys())
