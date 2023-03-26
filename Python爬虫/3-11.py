# 发送一个完整的 GET 请求

import chardet
import requests

url = 'http://www.tipdm.com/tipdm/index.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) Chrome/65.0.3325.181'}
rqg = requests.get(url, headers=headers, timeout=2)
print('状态码：', rqg.status_code)
print('编码：', rqg.encoding)
rqg.encoding = chardet.detect(rqg.content)['encoding']
print('修改后的编码：', rqg.encoding)
print('响应头：', rqg.headers)
print(rqg.text)
