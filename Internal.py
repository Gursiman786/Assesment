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

while True:
    userinput = input('What would you like to do:\n print all cars:\n Exit:\n')
    if userinput == '1':
        create_table()
    elif userinput == '2':
        print('Exiting...........')
        break
    else:
        print('Invalid input. Please enter a number from either 1 or 2!')
    if db:
    db.close()









