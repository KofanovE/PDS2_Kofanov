# Напишіть програму, яка змінює у таблиці 'student' поле 'id' на PRIMARY KEY.

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "53543Asd",
    database = "my_first_db"
)

mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE student CHANGE id id INT AUTO_INCREMENT PRIMARY KEY;")

mycursor.close()
mydb.close()
