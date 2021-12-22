import MySQLdb

db = MySQLdb.connect(
	host='localhost',
	user='root',
	passwd='',
	db='tutorials'
)
cur = db.cursor()

cur.execute('SELECT * from blogt')

for row in cur.fetchall():
	print(row)

db.close()
