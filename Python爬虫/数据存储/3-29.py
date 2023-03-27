import json
from lxml import etree
import requests
import chardet

# 将获取的文本使用 dump 方法写入 JSON 文件
url = "http://www.tipdm.com/tipdm/index.html"
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69"}
rqg = requests.get(url, headers=ua)
rqg.encoding = chardet.detect(rqg.content)['encoding']
html = rqg.content.decode('utf-8')
html = etree.HTML(html, parser=etree.HTMLParser(encoding='utf-8'))
content = html.xpath('//ul[starts-with(@id,"me")]/li//a/text()')
print('标题菜单的文本：', content)

with open('output.json', 'w') as fp:
    json.dump(content, fp)
