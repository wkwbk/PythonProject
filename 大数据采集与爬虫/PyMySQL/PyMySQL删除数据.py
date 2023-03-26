import pymysql

db = pymysql.connect(host="localhost", user="root", passwd="778057151", db="test")
cursor = db.cursor()

sql = "DELETE FROM employee WHERE age > '%d'" % 40

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
