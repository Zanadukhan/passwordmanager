
from getpass import getpass
import os
import sys
import mysql.connector

def editdb(query:str):
    """Edits field in DB and commits the change in the DB

    Args:
        query(str): SQL query that has been stored in a variable
    """
    mycursor.execute(query)
    mydb.commit()

    

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
            app = input('What is the name of the application? ').lower
            username = input('Enter your username: ')
            password = getpass('Enter your password: ')
            SQL = 'INSERT INTO logininfo (Application, Username, Password) VALUES (%s, %s, %s)'
            VAL = (app, username, password)
            mycursor.execute(SQL, VAL)
            mydb.commit()
            print(f'login info for {app} has been added')
        case 3:
            app = input('What application are you trying to change? ')
            choice = input('Are you editing the password or username? ')
            if choice == 'password':
                new_pass = getpass('what is your new password? ')
                edit = f"UPDATE logininfo SET Password = '{new_pass}' WHERE Application = '{app}'"
                editdb(edit)
                print(f'{app} has been updated with a new password')
            else:
                new_user = input('What is your new username?')
                edit = f"UPDATE logininfo SET Username = '{new_user}' WHERE Application = '{app}'"
                editdb(edit)
                print(f'{app} has been updated with a new username')
        case 4:
            pass
        case 5:
            sys.exit()
        case _:
            print('invalid option, try again')






  