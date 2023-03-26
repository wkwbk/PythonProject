import pymysql

db = pymysql.connect(host="localhost", user="root", passwd="778057151", db="test")
cursor = db.cursor()

sql = """INSERT INTO EMPLOYEE(first_name, last_name, age, sex, income)
VALUES('Mac', 'Su', 20, 'M', 5000)
"""

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
