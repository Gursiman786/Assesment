import sqlite3
SQLDATABASE = 'Cars.db'


def create_table():
    db = sqlite3.connect(SQLDATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM Cars;"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(rows)
    print('ID       Name        Top Speed')

    for row in rows:
        print(f"Row: {row[1]} {row[2]: > 200}")

    db.close()
