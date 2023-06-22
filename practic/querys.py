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
mycursor.execute("select * from love.day")
for i in mycursor:
    print(i)


mycursor.execute("select firstname,location from love.day")
for i in mycursor:
    print(i)

mycursor.execute("select * from love.day where id > 8 ")
for i in mycursor:
    print(i)

mycursor.execute("select * from love.day where id = 1")
for i in mycursor:
    print(i)

mycursor.execute("update love.day set firstname = 'yashu' where lastname = 'kakade' ")
mydb.commit()

mycursor.execute("select count(*),location from love.day group by location")
for i in mycursor:
    print(i)

mycursor.execute("delete from love.day where id = 11")
mydb.commit()

