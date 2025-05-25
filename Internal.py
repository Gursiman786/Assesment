import sqlite3
SQLDATABASE = 'Cars.db'


def create_table():
    db = sqlite3.connect(SQLDATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM Cars;"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print('ID       Name        Top Speed')
    print(rows)
    
    for row in rows:
        print(f"Row: {row[1]} {row[2]: > 200}")

    db.close()

def create_table2():
    db = sqlite3.connect(SQLDATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM Manufacturer;"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print('ID       Name of manufacturer')
    print(rows)
    

    for row in rows:
        print(f"Row: {row[1]} {row[2]}")

    db.close()

def create_table3():
    db = sqlite3.connect(SQLDATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM Engine;"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print('ID       Engine Type')
    print(rows)
    

    for row in rows:
        print(f"Row: {row[1]} {row[2]}")

    db.close()

while True:
    userinput = input('What would you like to do:\n Print all Cars: {1}\n Print all Manufacturers:{2}\n Print all Engines:{3}\n Exit:{4}\n')
    if userinput == '1':
        create_table()

    if userinput == '2':
        create_table2()

    if userinput == "3":  
        create_table3()

    elif userinput == '4':
        print('Exiting...........')
        break
    else:
        print('Invalid input. Please enter a number from either 1 or 2!')
    db.close()









