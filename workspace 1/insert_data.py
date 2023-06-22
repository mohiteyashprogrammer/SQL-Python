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

mycursor.execute("""insert into mydatabase.fsds values(1, 'yash', 'mohite', '2022-12-2','SQL','FSDS'), 
(2, 'yashika', 'gor', '2022-12-2','SQL','FSDS'),

(3, 'isha', 'suriyavanshi', '2022-12-2','SQL','FSDS'),

(4, 'siddhesh', 'patade', '2022-12-2','SQL','FSDS'),

(5, 'ankita', 'gurav', '2022-12-2','SQL','FSDS'),

(6, 'isha', 'ghoil', '2022-12-2','SQL','FSDS'),

(8, 'rutuja', 'rane', '2022-12-2','SQL','FSDS'),

(9, 'sarah', 'shake', '2022-12-2','mongodb','FSDS'),

(10, 'seema', 'yadav', '2022-1-1','python','FSDS'),

(11, 'pallavi', 'zakar', '2022-12-2','SQL','FSDS'),

(12, 'vaishanavi', 'manjeraker', '2023-1-2','python','FSDS'),

(13, 'samartha', 'patil', '2022-12-2','mongodb','FSDS'),

(14, 'rupali', 'regim', '2022-12-2','mongodb','FSDS'),

(15, 'bhoomi', 'manjrekar', '2022-8-15','oops','FSDS'),

(16, 'sanjana', 'malandaker', '2023-1-15','python','FSDS'),

(17, 'aarya', 'palgavker', '2023-1-10','SQL','FSDS'),

(18, 'nupur', 'more', '2023-1-2','SQL','FSDS'),

(19, 'divya', 'madhik', '2022-12-2','SQL','FSDS')""") 

mydb.commit()