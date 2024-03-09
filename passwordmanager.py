
from getpass import getpass
import os
import sys
import mysql.connector


mydb = mysql.connector.connect(
        host ='localhost',
        user ='root',
        password = os.environ.get('mysqlpass'),
        database = 'passwordmanager'
    )
# connects to mysql database, see dbeaver to see table data

mycursor = mydb.cursor()


while True:
    print('')
    print('1. View all entries')
    print('2. Add a new entry')
    print('3. edit an entry')
    print('4. delete an entry')
    print('5. exit')
    choice = int(input('Select your option from the menu: '))

    match choice:
        case 1:
            mycursor.execute('select * from logininfo')
            myresults = mycursor.fetchall()
            print('')
            for result in myresults:
                print(result)
        case 2:
            # new entry is added by taking in user entries and creating a new mysql tuple by inserting info into logininfo table)
            app = input('What is the name of the application? ')
            username = input('Enter your username: ')
            password = getpass('Enter your password: ')
            SQL = 'INSERT INTO logininfo (Application, Username, Password) VALUES (%s, %s, %s)'
            VAL = (app, username, password)
            mycursor.execute(SQL, VAL)
            mydb.commit()
            print(f'login info for {app} has been added')
        case 3:
            pass
        case 4:
            pass
        case 5:
            sys.exit()
        case _:
            print('invalid option, try again')






  