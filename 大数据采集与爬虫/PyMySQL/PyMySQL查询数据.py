import pymysql

db = pymysql.connect(host="localhost", user="root", passwd="778057151", db="test")
cursor = db.cursor()

sql = "SELECT * FROM employee WHERE income > '%d'" % 1000

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname = row[1]
        lname = row[2]
        age = row[3]
        sex = row[4]
        income = row[5]
        print("name=%s %s, age=%d, sex=%c, income=%.2f" % (fname, lname, age, sex, income))
except:
    import traceback
    traceback.print_exc()
    print("Error: unable to fetch data")

db.close()
