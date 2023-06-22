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


mycursor.execute("select id, email,batch from ineuron.students")
for i in mycursor:
    print(i)

mycursor.execute("select * from ineuron.students where id = 5")
for i in mycursor:
    print(i)


mycursor.execute("select * from ineuron.students where id >5")
for i in mycursor:
    print(i)


mycursor.execute("select * from ineuron.students where id < 2")
for i in mycursor:
    print(i)

mycursor.execute("update ineuron.students set batch = 'backoffic' where id = 5 ")
mydb.commit()

mycursor.execute("delete from ineuron.students where id = 5 ")
mydb.commit()

mycursor.execute("select count(*) from ineuron.students")
for i in mycursor:
    print(i)

mycursor.execute("select max(id) from ineuron.students")
for i in mycursor:
    print(i)


mycursor.execute("select min(id) from ineuron.students")
for i in mycursor:
    print(i)

mycursor.execute("select count(*), batch from ineuron.students group by batch")
for i in mycursor:
    print(i)
