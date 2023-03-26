from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"
}

url = "https://books.toscrape.com"

response = requests.get(url, headers=headers)
print("状态码：", response.status_code)
content = response.text

soup = BeautifulSoup(content, 'html.parser')
all_prices = soup.findAll("p", attrs={"class": "price_color"})
all_titles = soup.findAll("h3")

for titles in all_titles:
    link = titles.find("a")
    print("书名：", link.string)

for prices in all_prices:
    print("价格：", prices.string)
