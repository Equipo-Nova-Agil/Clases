import mysql.connector
from mysql.connector import Error




pdb = mysql.connector.connect(host='localhost', user='root', password='Dantesco93', database='misiontic')

cur = pdb.cursor()
cur.execute("Show tables;")

myresult = cur.fetchall()

print(myresult)
for i in myresult:
    print(i)
