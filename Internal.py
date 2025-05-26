'''THIS IS DATABASE ON CARS :)'''
import sqlite3
SQLDATABASE = 'Cars.db'

from colorama import Fore, Style

#This is the table relating to the Cars table of the database
def Cars():
    db = sqlite3.connect(SQLDATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM Cars;"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(Fore.CYAN + 'Name                         Top Speed KM/H' + Style.RESET_ALL)

    #prints out all the DATA
    for row in rows:
        print(Fore.YELLOW + f"{row[1]:35} {row[2]}" + Style.RESET_ALL)
 
    db.close()
#This is the table relating to the Maufacturuer table of the database
def Manufacturer():
    db = sqlite3.connect(SQLDATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM Manufacturer;"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(Fore.LIGHTMAGENTA_EX  + 'ID               Name of manufacturer' + Style.RESET_ALL)

    #prints out all the DATA
    for row in rows:
        print(Fore.YELLOW + f"{row[0]} {row[1]:25}" + Style.RESET_ALL)

    db.close()
#This is the table relating to the Engine table of the database
def Engine():
    db = sqlite3.connect(SQLDATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM Engine;"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(Fore.BLUE + 'ID       Engine Type' + Style.RESET_ALL)
 
    
 #prints out all the DATA
    for row in rows:
        print(Fore.YELLOW + f"{row[0]:3} {row[1]}" + Style.RESET_ALL)

    db.close()
# While true loop fpor userinput
while True:
    #variable 'Userinput'
    userinput = input('What would you like to do:\n Print all Cars: {1}\n Print all Manufacturers: {2}\n Print all Engines: {3}\n Exit: {4}\n')
    if userinput == '1':
        Cars()
        userinput = input('What would you like to do:\n Print all Cars: {1}\n Print all Manufacturers: {2}\n Print all Engines: {3}\n Exit: {4}\n')

    elif userinput == '2':
        Manufacturer()
        userinput = input('What would you like to do:\n Print all Cars: {1}\n Print all Manufacturers: {2}\n Print all Engines: {3}\n Exit: {4}\n')

    elif userinput == "3":  
        Engine()
        userinput = input('What would you like to do:\n Print all Cars: {1}\n Print all Manufacturers: {2}\n Print all Engines: {3}\n Exit: {4}\n')

    elif userinput == '4':
        print('Exiting...........')
        break
    else:    
        #For out of range inputs
        print('Invalid input. Please enter a number from either 1-4!')
        continue
       


    db.close()









