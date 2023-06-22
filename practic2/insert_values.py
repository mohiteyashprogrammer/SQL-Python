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
mycursor.execute("""insert into ME.i values(1,'yash mohite',22,5.8),
(2,'isha surtayavanshi',22,5.4),
(3,'isha gohil',22,5),
(4,'aditya bhosle',21,5.6),
(5,'karan malandaker',24,5.9),
(6,'ankita gurav',22,5.6),
(7,'dhanashree suryavanshi',21,5.9),
(8,'yashika gor',22,5.5),
(9,'varsha bagul',21,5.4),
(10,'siddhesh patade',22,5.7),
(11,'chirag darji',23,5.7),
(12,'rishsik mahajan',22,5.9),
(13,'karishma',24,5.6),
(14,'yash kakade',21,5.8),
(19,'vaishnavi manjeraker',23,5.5)""")

mydb.commit()
