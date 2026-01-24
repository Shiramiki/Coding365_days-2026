import mysql.connector
mydb =mysql.connector.connect(
    host="localhost",
    user ="user",
    password ="MyStrongPass123",
)

print(mydb)