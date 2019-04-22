import MySQLdb


db = MySQLdb.connect("localhost", "root", "mysql", "gry", charset='utf8')
cur = db.cursor()
sql = "INSERT INTO citys values ('123', '5', '6');"
for i in range(1,10):
    cur.execute(sql)
    db.commit()