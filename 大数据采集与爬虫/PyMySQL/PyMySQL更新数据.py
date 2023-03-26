import pymysql

db = pymysql.connect(host="localhost", user="root", passwd="778057151", db="test")
cursor = db.cursor()

sql = "UPDATE employee SET age=age + 1 WHERE sex='%c'" % 'M'

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
