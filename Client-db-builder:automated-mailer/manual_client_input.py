import sqlite3
import os

try:
    os.chdir('/Users/NAME/WORKINGDIR')
except OSError:
    print('Cannot change the Current Working Directory, look at code')

while True:
    while True :
        ncf = input('New client first name: ')
        ncl = input('New client last name: ')
        tit = input('New client title: ')
        mail = input('New client e-mail: ')
        comp = input('New client company: ')

        var = input('Are you happy with this entry? (y/n) ')
        if var == 'y' :
            print('Ok, proceeding')
            break
        else :
            print('Ok, restart')
            continue

    conn = sqlite3.connect('clients.sqlite')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Clients
                (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT,
                title TEXT, e_mail TEXT, company TEXT)''')

    cur.execute('''INSERT INTO Clients (first_name, last_name, title, e_mail, company)
                VALUES (?, ?, ?, ?, ?)''', (ncf, ncl, tit, mail, comp))
    conn.commit()

    cur.execute('SELECT id, first_name, last_name, title, e_mail, company FROM Clients')
    for row in cur :
        print(row)

    cur.close()

    rest = input('Add another client? (y/n)')
    if rest == 'y' :
        continue
    else: break

cur.close()
quit()
