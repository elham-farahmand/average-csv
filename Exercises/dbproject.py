import re
import mysql.connector

def email_check(email):
    res = re.search(r'^[a-zA-Z0-9]+\@.+\..+$', email)
    if ( res != None):
        return True
    else:
        return False

def pass_check(password):
    res = re.search(r'^[a-zA-Z0-9]+$', password)
    if ( res != None):
        return True
    else:
        return False

    
email_input = input('Insert your Email: ')
while (email_check(email_input) != True):
    email_input = input('Email is not correct. A valid Email is like: example@example.exapmle. Insert your Email: ')

password_input = input('Insert your password: ')
while (pass_check(password_input) != True):
    password_input = input('Password is not correct. A valid password includes numbers and letters. Insert your Password: ')

dbname = 'info'
tablename = 'userpass'
cnx = mysql.connector.connect(user='root', password = '', host = '127.0.0.1', database = dbname)
cursor = cnx.cursor()
cursor.execute('INSERT INTO %s VALUES (\'%s\',\'%s\')' % (tablename, email_input, password_input))
cnx.commit()
cnx.close()
    