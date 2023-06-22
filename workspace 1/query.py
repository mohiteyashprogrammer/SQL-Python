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

mycursor.execute("select * from mydatabase.fsds")
for i in mycursor:
    print(i)

mycursor.execute("select studentid, lastname,cource_name from mydatabase.fsds")
for i in mycursor:
    print(i)


mycursor.execute("select * from mydatabase.fsds where firstname = 'yashika'")
for i in mycursor:
    print(i)

mycursor.execute("select * from mydatabase.fsds where studentid = 8")
for i in mycursor:
    print(i)

mycursor.execute("select * from mydatabase.fsds where firstname = 'yash' and class = 'SQL'")
for i in mycursor:
    print(i)


mycursor.execute("select * from mydatabase.fsds where studentid > 10 ")
for i in mycursor:
    print(i)


mycursor.execute("select * from mydatabase.fsds where studentid < 10 ")
for i in mycursor:
    print(i)

mycursor.execute("update mydatabase.fsds set  firstname = 'arya' where studentid = 17")
mydb.commit()

mycursor.execute("update mydatabase.fsds set  class = 'mongodb' where studentid = 17")
mydb.commit()

mycursor.execute("delete from mydatabase.fsds where studentid = 11")
mydb.commit()



mycursor.execute("select min(studentid) from mydatabase.fsds")
for i in mycursor:
    print(i)

mycursor.execute("select max(studentid) from mydatabase.fsds")
for i in mycursor:
    print(i)

mycursor.execute("select count(*) from mydatabase.fsds")
for i in mycursor:
    print(i)

mycursor.execute("update mydatabase.fsds set class = 'mongoDB' where studentid between 1 and 5 ")
mydb.commit()


mycursor.execute("update mydatabase.fsds set class = 'python' where studentid between  15 and 19 ")
mydb.commit()

mycursor.execute("select count(*) , class from mydatabase.fsds group by class")
for i in mycursor:
    print(i)


