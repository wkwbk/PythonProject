import pymysql
connector = pymysql.connect(host="localhost", user="root", password="778057151", port=3306)
cursor = connector.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version:", data)
cursor.execute("CREATE DATABASE test DEFAULT CHARACTER SET utf8mb4")
connector.close()
