import pymysql
import requests
import chardet
from bs4 import BeautifulSoup

# 使用 connect 函数链接数据库
conn = pymysql.connect(host="localhost", user="root", password="778057151", port=3306, database="test")
cursor = conn.cursor()
sql = """CREATE TABLE IF NOT EXISTS class(
id int(10) PRIMARY KEY AUTO_INCREMENT,
name varchar(20) NOT NULL,
text varchar(20) NOT NULL)
"""
cursor.execute(sql)
cursor.execute('SHOW TABLES')

url = "http://www.tipdm.com/tipdm/index.html"
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69"}
rqg = requests.get(url, headers=ua)
rqg.encoding = chardet.detect(rqg.content)['encoding']
html = rqg.content.decode('utf-8')
soup = BeautifulSoup(html, 'lxml')
target = soup.title.string
print('标题的内容', target)

title = 'tipdm'
sql = 'INSERT INTO class(name, text)VALUES(%s, %s)'
cursor.execute(sql, (title, target))

conn.commit()
data = cursor.execute('SELECT * FROM class')
data = cursor.fetchone()
print('查询获取的结果：', data)

cursor.close()