import requests
import json

url = "https://www.ptpress.com.cn/bookinfo/getBookListForWS"
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69"}

return_data = requests.get(url, headers=ua).text
data = json.loads(return_data)
news = data['data']
for n in news:
    bookName = n['bookName']
    author = n['author']
    price = n['price']
    print("新书名：", bookName, "\n", "作者：",  author, "\n", "价格：", price, "\n")
