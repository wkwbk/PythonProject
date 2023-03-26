# 使用正则表达式查找网页内容中的 title 内容

import re
import requests
import chardet

url = "http://www.tipdm.com/tipdm/index.html"
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69"}
rqg = requests.get(url, headers=ua)
rqg.encoding = chardet.detect(rqg.content)["encoding"]
title_pattern = r'(?<=<title>).*?(?=</title>)'
title_com = re.compile(title_pattern, re.M | re.S)
title_search = re.search(title_com, rqg.text)
title = title_search.group()
print("标题内容：", title)
print("标题内容：", re.findall(r'<title>(.*?)</title>', rqg.text))
