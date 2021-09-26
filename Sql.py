
import mysql.connector
from mysql.connector import Error




connection = mysql.connector.connect(host='localhost', user='root', password='Dantesco93', database='mydb')

print(connection)

