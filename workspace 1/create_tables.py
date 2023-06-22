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

mycursor.execute("create table mydatabase.fsds(studentid int, firstname varchar(50), lastname varchar(50),registeration DATE, class varchar(20),cource_name varchar(50))")