
from getpass import getpass
import os
import sys
import base64
import mysql.connector

def editdb(query:str):
    """Edits field in DB and commits the change in the DB

    Args:
        query(str): SQL query that has been stored in a variable
    """
    mycursor.execute(query)
    mydb.commit()
    print('')

def passwordencryption(pwd):
    return base64.b64encode(pwd.encode('utf-8'))

def decodepassword(encrypted):
    return base64.b64decode(encrypted).decode('utf-8')
    
# TODO: Add Salting and Hashing Function to every password occurance
# TODO: Initial DB creation for first time use
# TODO: Add a new function for getting unhashed and desalted password or figure out how to return
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
            # returns all rows in the logininfo table as tuples
            mycursor.execute('select * from logininfo')
            myresults = mycursor.fetchall()
            print('')
            for result in myresults:
                result = list(result)
                decrypted = decodepassword(result[3])
                result[3] = decrypted
                print(result)
        case 2:
            # new entry is added by taking in user entries and creating a new mysql tuple by inserting info into logininfo table
            app = input('What is the name of the application? ')
            username = input('Enter your username: ')
            password = getpass('Enter your password: ')
            # TODO: create Password generator
            encryptpass = passwordencryption(password)
            SQL = 'INSERT INTO logininfo (Application, Username, Password) VALUES (%s, %s, %s)'
            VAL = (app, username, encryptpass)
            mycursor.execute(SQL, VAL)
            mydb.commit()
            print(f'login info for {app} has been added')
        case 3:
            app = input('What application are you trying to change? ')
            # TODO: check if application exists
            choice = input('Are you editing the password or username? ')
            if choice == 'password':
                # this section allows the user to change the current password for chosen app
                new_pass = getpass('what is your new password? ')
                new_pass = passwordencryption(new_pass)
                edit = f"UPDATE logininfo SET Password = '{new_pass}' WHERE Application = '{app}'"
                editdb(edit)
                print(f'{app} has been updated with a new password')
            else:
                # this section allows the user to change the username for the chosen app
                new_user = input('What is your new username?')
                edit = f"UPDATE logininfo SET Username = '{new_user}' WHERE Application = '{app}'"
                editdb(edit)
                print(f'{app} has been updated with a new username')
        case 4:
            choice = input('What application would you like to delete? ')
            delete = f"DELETE FROM logininfo WHERE Application = '{choice}'"
            editdb(delete)
            print(f'{choice} has been deleted from the database)')
        case 5:
            # quits program
            sys.exit()
        case _:
            print('invalid option, try again')
  