import pypyodbc
import datetime

driver = 'driver={SQL Server}'
username = ''
password = ''
server = ''
database = ''


conn = pypyodbc.connect(driver=driver, server=server, database=database, uid=username, pwd=password)


#use the SQLServer login, not AD

cur = conn.cursor()
conn.execute()

#changing the blank space in end= to a ',' will make it comma-delimited
for d in cur.description: 
    print (d[0], end=" ")


for row in cur.fetchall():
    for field in row:
        print(field, end=" ")
    print('')

#constructing the sql for this doesn't seem like it'd be too hard...

#close the connection
cur.close()
conn.close()

#how to check for NULL fields?  should that be done in the initial file check?
