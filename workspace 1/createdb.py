import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()

mycursor.execute("show databases")
for i in mycursor:
    print(i)

mycursor.execute("create database mydatabase")