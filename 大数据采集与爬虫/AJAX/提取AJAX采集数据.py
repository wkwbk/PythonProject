from urllib.parse import urlencode
import requests
import pymysql

original_url = "https://www.autohome.com.cn/ashx/AjaxIndexHotCarByDsj.ashx?"
requests_headers = {
    "Referer": "https://www.autohome.com.cn/beijing/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69",
    "X-Requested-With": "XMLHttpRequest"
}


def get_one(cityid):
    p = {"cityid": cityid}
    complete_url = original_url + urlencode(p)
    try:
        resource = requests.get(url=complete_url, params=requests_headers)
        if resource.status_code == 200:
            return resource.json()
    except requests.ConnectionError as e:
        print("Error", e.args)


def parse(json):
    if json:
        item = json[0].get("Name")
        print(item)


def parse_tow(json):
    if json:
        for i in json:
            for b in i.get("SeriesList"):
                item = b.get("Name")
                print(item)


def parse_three(json):
    if json:
        # 创建数据库
        db1 = pymysql.connect(host="localhost", user="root", password="778057151", port=3306)
        cursor1 = db1.cursor()
        cursor1.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'ajax'")
        result = cursor1.fetchone()
        if result:
            print("数据库已存在，无需创建")
        else:
            cursor1.execute("CREATE DATABASE ajax DEFAULT CHARACTER SET utf8mb4")
            print("创建数据库成功")
        db1.close()
        # 创建表
        db2 = pymysql.connect(host="localhost", user="root", passwd="778057151", port=3306, database="ajax")
        cursor2 = db2.cursor()
        cursor2.execute("DROP TABLE IF EXISTS ajax")
        sql = """
            CREATE TABLE ajax(
            car_name char(20) NOT NULL,
            id int(10) NOT NULL AUTO_INCREMENT,
            PRIMARY KEY (id))ENGINE InnoDB DEFAULT CHARSET=utf8mb4"""
        cursor2.execute(sql)
        print("创建表成功")
        # 插入数据
        for i in json:
            for b in i.get("SeriesList"):
                item_list1 = b.get("Name")
                item_list2 = b.get("Id")
                print(item_list1 + "：" + str(item_list2))
                sql = "INSERT INTO ajax (car_name, id) VALUES (%s, %s)"
                try:
                    cursor2.execute(sql, (item_list1, item_list2))
                    db2.commit()
                except:
                    db2.rollback()
        db2.close()


if __name__ == '__main__':
    city_list = [{"北京": "110100"}, {"重庆": "500100"}, {"上海": "310100"}]
    for city in city_list:
        jo = get_one(city.values())
        parse_three(jo)
