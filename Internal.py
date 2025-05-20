import sqlite3
SQLDATABASE = 'Cars.db'

db = sqlite3.connect(SQLDATABASE)
cursor = db.cursor()
sql = "Select * from Cars;"
cursor.execute(sql)
