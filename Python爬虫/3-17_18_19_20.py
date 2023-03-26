import requests
from lxml import etree

url = "http://www.tipdm.com/tipdm/index.html"
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69"}
rqg = requests.get(url, headers=ua)
html = rqg.content.decode('utf-8')
html = etree.HTML(html, parser=etree.HTMLParser(encoding='utf-8'))

# 使用表达式定位 head 和 title 节点
result = html.xpath('head')
print('名称定位结果：', result)
result1 = html.xpath('/html/head/title')
print('节点层级定位结果：', result1)
result2 = html.xpath('title')
print('名称定位 title 节点结果：', result2)
result3 = html.xpath('//title')
print('搜索定位 title 节点结果：', result3)

# 使用谓语定位 header 和 ul 节点
result4 = html.xpath('//header[@class]')
print('class 属性定位结果：', result4)
result5 = html.xpath('//ul[@id="menu"]')
print('id 属性定位结果：', result5)

# 定位并获取 title 节点内的文本内容
title = html.xpath('//title/text()')
print('title 节点的文本内容：', title)

# 提取 ul 节点下的所有文本内容和对应的链接
content = html.xpath('//ul[starts-with(@id, "me")]/li//a/text()')
for i in content:
    print(i)
url_list = html.xpath('//ul[starts-with(@id, "me")]/li//a/@href')
for i in url_list:
    print(i)
target = html.xpath('//ul[starts-with(@id, "me")]')
target_text = target[0].xpath('string(.)').strip()
print('节点下的全部文本内容：', target_text)
