# Напишіть програму, яка створює нову базу даних 'my_first_db'

import  mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "53543Asd"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE my_first_db")

mycursor.close()
mydb.close()