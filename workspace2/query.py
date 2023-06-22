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

mycursor.execute("select * from schooldb.students")
for i in mycursor:
    print(i)

mycursor.execute("select  studentid, firstname,house from schooldb.students")
for i in mycursor:
    print(i)


mycursor.execute("select * from schooldb.students where studentid = 14")
for i in mycursor:
    print(i)

mycursor.execute("select * from schooldb.students where studentid  < 4")
for i in mycursor:
    print(i)

mycursor.execute("select * from schooldb.students where firstname = 'isha' ")
for i in mycursor:
    print(i)

mycursor.execute("select * from schooldb.students where house = 'green'")
for i in mycursor:
    print(i)

mycursor.execute("update schooldb.students set firstname = 'saam' where studentid = 18")
mydb.commit()

mycursor.execute("update schooldb.students set class = 'job' where studentid = 25")
mydb.commit()

mycursor.execute("delete from schooldb.students where studentid = 25")
mydb.commit()

mycursor.execute("delete from schooldb.students where studentid = 2")
mydb.commit()

mycursor.execute("select min(studentid) from schooldb.students")
for i in mycursor:
    print(i)

mycursor.execute("select max(studentid) from schooldb.students")
for i in mycursor:
    print(i)

mycursor.execute("select count(*) from schooldb.students")
for i in mycursor:
    print(i)

mycursor.execute("update schooldb.students set class = 'business' where studentid = 4 ")
mydb.commit()

mycursor.execute("select count(*) ,class from schooldb.students group by class")
for i in mycursor:
    print(i)

mycursor.execute("select count(*) ,house from schooldb.students group by house")
for i in mycursor:
    print(i)



