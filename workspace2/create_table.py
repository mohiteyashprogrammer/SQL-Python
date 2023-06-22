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

mycursor.execute("create table schooldb.students(studentid int, firstname varchar(50), lastname varchar(50),house varchar(50),class varchar(50),phonenumber int(10))")