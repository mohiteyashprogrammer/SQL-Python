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

mycursor.execute("""insert into schooldb.students values(1, 'yash', 'mohite', 'blue','FSDS',8424),
(2, 'isha', 'suryavanshi', 'blue','MBA',89421),
(3, 'ankita', 'gurav', 'red','MBA',94758),
(4, 'siddhesh', 'patade', 'green','MPSC',9224),
(5, 'aniket', 'dhadave', 'blue','engineer',8424),
(6, 'prajwal', 'kore', 'blue','CS',8424),
(7, 'abhishake', 'todkar', 'yellow','CS',8424),
(8, 'isha', 'gohil', 'blue','MBA',9478),
(9, 'rutuja', 'rane', 'yellow','MBA',1478),
(10, 'seema', 'yadav', 'green','bcom',99624),
(11, 'vaishnavi', 'manjrekar', 'red','MBA',8774),
(12, 'bhoomi', 'manjrekar', 'blue','FSDS',81487),
(13, 'tejal', 'kakade', 'green','MBA',8282),
(14, 'yash', 'kakade', 'yellow','CA',77745),
(15, 'varsha', 'bagul', 'red','MBA',87845),
(16, 'pooja', 'patil', 'yellow','medical',7458),
(17, 'yashika', 'gor', 'blue','FSDS',1478),
(18, 'samartha', 'patil', 'green','MBA',47845),
(19, 'chirag', 'darji', 'red','accounts',8854),
(20, 'rushikesh', 'monde', 'red','accounts',9856),
(21, 'raj', 'bagul', 'blue','police bharti',4587),
(22, 'vinay', 'patil', 'yellow','police bharti',84887),
(23, 'shubham', 'pice', 'red','police bharti',8888),
(24, 'prathmesh', 'parab', 'green','business',8784),
(25, 'prathmesh', 'satpute', 'blue','business',88556)""")

mydb.commit()

