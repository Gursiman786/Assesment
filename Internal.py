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
    userinput = input('What would you like to do:\n print all cars: {1}\n print all Manufacturers:{2}\n print all Engines:{3}\n Exit:{4}\n')
    if userinput == '1':
        create_table()


        userinput = input('What would you like to do:\n print all cars: {1}\n  print all Manufacturers:{2}\n print all Engines:{3}\n Exit:{4}\n')
    if userinput == '2':
        create_table2()


        userinput = input('What would you like to do:\n print all cars: {1}\n  print all Manufacturers:{2}\n print all Engines:{3}\n Exit:{4}\n')
    if userinput == '3':
        create_table3()


        userinput = input('What would you like to do:\n print all cars: {1}\n  print all Manufacturers:{2}\n print all Engines:{3}\n Exit:{4}\n')
    elif userinput == '4':
        print('Exiting...........')
        break
    else:
        print('Invalid input. Please enter a number from either 1 or 2!')
    db.close()









