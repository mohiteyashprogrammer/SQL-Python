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
mycursor.execute("select * from ME.i")
for i in mycursor:
    print(i)

mycursor.execute("select name,id from ME.i")
for i in mycursor:
    print(i)

mycursor.execute("select * from ME.i where id = 3")
for i in mycursor:
    print(i)

mycursor.execute("select * from ME.i where id > 10")
for i in mycursor:
    print(i)

mycursor.execute("select * from ME.i where name = 'yash mohite'")
for i in mycursor:
    print(i)

mycursor.execute("select * from ME.i where hight = 5.7")
for i in mycursor:
    print(i)

mycursor.execute("update ME.i set age = 25 where id = 1 ")
mydb.commit()

mycursor.execute("delete from ME.i where id = 19")
mydb.commit()

mycursor.execute("select count(*) from ME.i")
for i in mycursor:
    print(i)

mycursor.execute("select count(*),hight from ME.i group by hight")
for i in mycursor:
    print(i)

mycursor.execute("select min(hight) from ME.i")
for i in mycursor:
    print(i)

mycursor.execute("select max(hight) from ME.i")
for i in mycursor:
    print(i)


