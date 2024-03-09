import mysql.connector
import os, sys


mydb = mysql.connector.connect(
        host ='localhost',
        user ='root',
        password = os.environ.get('mysqlpass'),
        database = 'passwordmanager'
    )
# connects to mysql database, see dbeaver to see table data

mycursor = mydb.cursor()


while True:
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
            print('')
        case 2:
            loginID = int(input('Enter the entry #: '))
            app = input('What is the name of the application? ')
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            SQL = 'INSERT INTO logininfo (LoginID, Application, Username, Password) VALUES (%s, %s, %s, %s)'
            VAL = (loginID, app, username, password)
            mycursor.execute(SQL, VAL)
            mydb.commit()
            print('new entry added')
        case 3:
            pass
        case 4:
            pass
        case 5:
            sys.exit()
        case _:
            print('invalid option, try again')







# SQL = 'INSERT INTO logininfo (LoginID, Application, Username, Password) VALUES (%s, %s, %s, %s)'
# VAL = (1, "test", 'admin', 'password')

  