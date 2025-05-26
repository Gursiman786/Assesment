import sqlite3
SQLDATABASE = 'Cars.db'

from colorama import Fore, Style


def Cars():
    db = sqlite3.connect(SQLDATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM Cars;"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(Fore.CYAN + 'Name                         Top Speed KM/H' + Style.RESET_ALL)

    
    for row in rows:
        print(Fore.YELLOW + f"{row[1]:35} {row[2]}" + Style.RESET_ALL)
 
    db.close()

def Manufacturer():
    db = sqlite3.connect(SQLDATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM Manufacturer;"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(Fore.LIGHTMAGENTA_EX  + 'ID               Name of manufacturer' + Style.RESET_ALL)

    
    for row in rows:
        print(Fore.YELLOW + f"{row[0]} {row[1]:25}" + Style.RESET_ALL)

    db.close()

def Engine():
    db = sqlite3.connect(SQLDATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM Engine;"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(Fore.BLUE + 'ID       Engine Type' + Style.RESET_ALL)
 
    

    for row in rows:
        print(Fore.YELLOW + f"{row[0]:3} {row[1]}" + Style.RESET_ALL)

    db.close()

while True:
    userinput = input(Fore.LIGHTMAGENTA_EX + 'What would you like to do:\n Print all Cars: {1}\n Print all Manufacturers: {2}\n Print all Engines: {3}\n Exit: {4}\n' + Style.RESET_ALL)
    if userinput == '1':
        Cars()
       userinput = input('What would you like to do:\n Print all Cars: {1}\n Print all Manufacturers: {2}\n Print all Engines: {3}\n Exit: {4}\n')

    if userinput == '2':
        Manufacturer()
        userinput = input('What would you like to do:\n Print all Cars: {1}\n Print all Manufacturers: {2}\n Print all Engines: {3}\n Exit: {4}\n')

    if userinput == "3":  
        Engine()
        userinput = input('What would you like to do:\n Print all Cars: {1}\n Print all Manufacturers: {2}\n Print all Engines: {3}\n Exit: {4}\n')

    if userinput == '4':
        print('Exiting...........')
        break
    else:
        print('Invalid input. Please enter a number from either 1-4!')
    db.close()









