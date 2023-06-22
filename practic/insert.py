
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
mycursor.execute('''insert into love.day values(1,'yash','mohite','andheri'),
(2,'yash','kakade','andheri'),
(3,'karan','malandaker','pune'),
(4,'isha','suryavanshi','vasai'),
(5,'isha','gohil','ghatkopar'),
(6,'yashika','gor','parle'),
(7,'sanjana','malandaker','andheri'),
(8,'seema','yadav','jogeshwary'),
(9,'siddesh','patade','nalasopara'),
(10,'chirag','dargi','andheri'),
(11,'vaishnavi','manjeraker','parla')''')
mydb.commit()