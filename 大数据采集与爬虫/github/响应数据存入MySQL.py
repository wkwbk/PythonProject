import requests
import pymysql

search_content = "spider"
api_url = f"https://api.github.com/search/repositories?q={search_content}"
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69"}

print("--------------------------------- GET 请求 ---------------------------------")

req = requests.get(api_url, headers=ua)
print("状态码：", req.status_code)

req_dic = req.json()
print(f"与 {search_content} 有关的库总数：", req_dic["total_count"])
print("本次请求是否完整：", req_dic["incomplete_results"])

req_dic_items = req_dic["items"]
print("当前页面返回的项目数量：", len(req_dic_items))

print("--------------------------------- 创建 github 数据库 ---------------------------------")

# db1 = pymysql.connect(host="localhost", user="root", password="778057151", port=3306)
# cursor1 = db1.cursor()
# cursor1.execute("CREATE DATABASE github DEFAULT CHARACTER SET utf8mb4")
# db1.close()

db1 = pymysql.connect(host="localhost", user="root", password="778057151", port=3306)
cursor1 = db1.cursor()
cursor1.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'github'")
result = cursor1.fetchone()
if result:
    print("数据库已存在，无需创建")
else:
    cursor1.execute("CREATE DATABASE github DEFAULT CHARACTER SET utf8mb4")
    print("创建数据库成功")
db1.close()

print("--------------------------------- 创建 webapi 表 ---------------------------------")

db2 = pymysql.connect(host="localhost", user="root", password="778057151", port=3306, database="github")
cursor2 = db2.cursor()
cursor2.execute("DROP TABLE IF EXISTS webapi")
sql1 = """CREATE TABLE webapi(
index_id int(10) NOT NULL AUTO_INCREMENT,
github_id int(10) NOT NULL,
full_name char(100) NOT NULL,
html_url char(100) NOT NULL,
PRIMARY KEY (index_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"""
cursor2.execute(sql1)
print("创建表成功")

print("--------------------------------- 写入数据 ---------------------------------")

for index_id, key in enumerate(req_dic_items, start=1):
    print("项目序号:", index_id, "|", "项目 ID:", key["id"], "|", "项目名称:", key["full_name"], "|", "项目链接:", key["html_url"])
    sql2 = "INSERT INTO webapi(index_id, github_id, full_name, html_url) VALUES(%s, %s, %s, %s)"
    try:
        cursor2.execute(sql2, (index_id, key["id"], key["full_name"], key["html_url"]))
        db2.commit()
    except:
        print("Error")
        db2.rollback()

db2.close()
