import requests
from lxml import etree

# 使用 HTML 类将网页内容初始化并打印
url = "http://www.tipdm.com/tipdm/index.html"
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69"}
rqg = requests.get(url, headers=ua)
html = rqg.content.decode('utf-8')
html = etree.HTML(html, parser=etree.HTMLParser(encoding='utf-8'))
result = etree.tostring(html, encoding='utf-8', pretty_print=True, method="html")
print("修正后的 HTML：", result)
print("格式化后的 HTML：", result.decode('utf-8'))

# 从本地文件导入 HTML 并初始化
html_local = etree.parse('./test.html', etree.HTMLParser(encoding='utf-8'))
result = etree.tostring(html_local)
print("本地文件导入的 HTML：", result)
print("格式化后的 HTML：", result.decode('utf-8'))
