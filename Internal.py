import sqlite3
from colorama import Fore, Style
'''Start of the best Cars database ever :)'''
SQLDATABASE = 'Cars.db'

# This is the table relating to the Cars table of the database
'''Defining Cars table'''
def Cars():
    db = sqlite3.connect(SQLDATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM Cars;"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(Fore.CYAN + 'Name                         Top Speed KM/H' + Style.RESET_ALL)

    # Prints out all the data
    for row in rows:
        print(Fore.YELLOW + f"{row[1]:35} {row[2]}" + Style.RESET_ALL)
    
    db.close()

# This is the table relating to the Manufacturer table of the database
'''Defining Maunfuacturer table'''
def Manufacturer():
    db = sqlite3.connect(SQLDATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM Manufacturer;"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(Fore.LIGHTMAGENTA_EX + 'ID               Name of manufacturer' + Style.RESET_ALL)

    # Prints out all the data
    for row in rows:
        print(Fore.GREEN + f"{row[0]} {row[1]:25}" + Style.RESET_ALL)
    
    db.close()

# This is the table relating to the Engine table of the database
'''Defining Engine table'''
def Engine():
    db = sqlite3.connect(SQLDATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM Engine;"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(Fore.BLUE + 'ID       Engine Type' + Style.RESET_ALL)

    # Prints out all the data
    for row in rows:
        print(Fore.LIGHTMAGENTA_EX + f"{row[0]:3} {row[1]}" + Style.RESET_ALL)
        

    db.close()

# While loop for user input
'''INPUT for getting data from tables'''
while True:
    userinput = input(Fore.RED + 'What would you like to do:\nPrint all Cars: {1}\nPrint all Manufacturers: {2}\nPrint all Engines: {3}\nExit: {4}\n' + Style.RESET_ALL)

    if userinput == '1':
        Cars()

    elif userinput == '2':
        Manufacturer()

    elif userinput =="3":
        Engine()

    elif userinput == '4':
        print(Fore.RED + 'Exiting...........')
        break

    else:
        # For out-of-range inputs
        print( Fore.GREEN + 'Invalid input. Please enter a number from either 1,2,3,4!')