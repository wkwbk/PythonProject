from bs4 import BeautifulSoup

import requests
import chardet

# 将网页内容转化为 BeautifulSoup 对象并格式化输出
print("------------------------------- 3-21 -------------------------------")
url = "http://www.tipdm.com/tipdm/index.html"
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69"}
rqg = requests.get(url, headers=ua)
rqg.encoding = chardet.detect(rqg.content)['encoding']
html = rqg.content.decode('utf-8')
soup = BeautifulSoup(html, "lxml")
print('输入格式化的 BeautifulSoup 对象：', soup.prettify())

# 通过 find_all 方法获取全部同名 Tag 对象
print("\n------------------------------- 3-22 -------------------------------")
print('获取 head 标签：', soup.head)
soup.title
print('获取第一个 a 标签：', soup.body.a)
print('所有名称为 a 的标签个数', len(soup.find_all('a')))

# 获取 Tag 对象的 name 属性并修改属性值
print("\n------------------------------- 3-23 -------------------------------")
print('soup 的 name：', soup.name)
print('a 标签的 name：', soup.a.name)
tag = soup.a
print('tag 的 name：', tag.name)
print('tag 的内容：', tag)
tag.name = 'b'
print('修改 name 后 tag 的内容：', tag)

# 获取 Tag 对象的 attributes 属性并修改属性值
print("\n------------------------------- 3-24 -------------------------------")
print('Tag 对象的全部属性：', tag.attrs)
print('class 属性的值：', tag['class'])
tag['class'] = 'Logo'
print('修改后 Tag 对象的属性：', tag.attrs)
tag['id'] = 'logo'
del tag['class']
print('修改后 tag 的内容：', tag)

# 获取 title 标签中的 NavigableString 对象并替换内容
print("\n------------------------------- 3-25 -------------------------------")
tag = soup.title
print('Tag 对象中包含的字符串：', tag.string)
print('tag.string 的类型: ', type(tag.string))
tag.string.replace_with('泰迪科技')
print('替换后的内容：', tag.string)

# 查看 BeautifulSoup 对象的类型和相关属性
print("\n------------------------------- 3-26 -------------------------------")
print('soup 的类型：', type(soup))
print('BeautifulSoup 对象的特殊 name 属性：', soup.name)
print('soup.name 的类型：', type(soup.name))
print('BeautifulSoup 对象的 attribute 属性：', soup.attrs)

# 获取节点的 Comment 对象并输出内容
print("\n------------------------------- 3-27 -------------------------------")
markup = '<c><!--This is a markup--></b>'
soup_comment = BeautifulSoup(markup, 'lxml')
comment = soup_comment.c.string
print('注释的内容：', comment)
print('注释的类型：', type(comment))

# 使用 find_all 方法定位节点并使用 get 和 get_text 方法获取节点的链接和文本
print("\n------------------------------- 3-28 -------------------------------")
print('名为 title 的全部子节点：', soup.find_all("title"))
print('title 子节点的文本内容：', soup.title.string)
print('使用 get_text() 获取的文本内容：', soup.title.get_text())
target = soup.find_all('ul', class_='menu')
print('CSS 类名匹配获取的节点：', target)
target = soup.find_all(id='menu')
print('关键字 id 匹配的节点：', target)
target = soup.ul.find_all('a')
print('所有名称为 a 的节点：', target)
urls = []
text = []
for tag in target:
    urls.append(tag.get('href'))
    text.append(tag.get_text())
for url in urls:
    print(url)
for i in text:
    print(i)
