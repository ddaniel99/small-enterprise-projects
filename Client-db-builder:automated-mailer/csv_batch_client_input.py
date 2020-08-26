import csv
import os
import sqlite3

try:
    os.chdir('/Users/NAME/WORKINGDIR')
except OSError:
    print('Cannot change the Current Working Directory, look at code')

conn = sqlite3.connect('clients.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Clients
            (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT,
            title TEXT, e_mail TEXT, company TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Hedge_Reqs
            (from_id INTEGER, hedge_req TEXT)''')

fname = input('Please enter a CSV file name: ')
with open(fname) as file:
    reader = csv.reader(file)
    next(reader)
    for first_name, last_name, title, e_mail, company, hedge_req in reader:
        cur.execute('''INSERT INTO Clients (first_name, last_name, title, e_mail, company)
                    VALUES (?, ?, ?, ?, ?)''', (first_name, last_name, title, e_mail, company))
        conn.commit()
    cur.close()
cur.close()

quit()
