import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Nice0145",
    database = "shop"
)
print(mydb)