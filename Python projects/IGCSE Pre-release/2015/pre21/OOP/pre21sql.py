import mysql.connector
mydb =mysql.connector.connect(
    host="localhost",
    user ="user",
    password ="MyStrongPass123",
    database="pre21sql"
)

print(mydb)
mycursor = mydb.cursor() #object that communicates with entire databas

# mycursor.execute("CREATE DATABASE pre21sql")

mycursor.execute("SHOW TABLES")
for db in mycursor:
    print(db)

# mycursor.execute("CREATE TABLE tempdata (time VARCHAR(255), temp FLOAT)")