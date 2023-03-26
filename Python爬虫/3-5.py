# 发送完整 HTTP 请求

import urllib3

http = urllib3.PoolManager()
url = 'http://www.tipdm.com/tipdm/index.html'
ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) Chrome/65.0.3325.181'}
tm = urllib3.Timeout(connect=1.0, read=3.0)
rq = http.request('GET', url, headers=ua, timeout=tm, retries=5, redirect=4)

print('服务器响应码：', rq.status)

print('获取的内容：', rq.data.decode('utf-8'))
