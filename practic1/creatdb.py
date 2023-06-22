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

#mycursor.execute("create database ineuron")

#mycursor.execute("create table ineuron.students(id int, firstname varchar(50),lastname varchar(50),email varchar(50),batch varchar(50))")

mycursor.execute("""insert into ineuron.students values(1,'yash','mohite','yash@gmail.com','FSDS'),
(2,'isha','gohil','isha@gmail.com','FSDS'),
(3,'isha','suryavanshi','isha18@gmail.com','FSDS'),
(4,'yashika','gore','yashika@gmail.com','FSDS'),
(5,'seema','yadav','seema@gmail.com','jobless'),
(6,'vaishnavi','manjeraker','vaisu@gmail.com','MBA'),
(7,'rutuja','rane','rutu@gmail.com','MBA')""")

mydb.commit()


mycursor.execute("select * from ineuron.students")
for i in mycursor:
    print(i)
