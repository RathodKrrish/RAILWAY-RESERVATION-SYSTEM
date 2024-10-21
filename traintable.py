import mysql.connector
import pandas as pd

#------------->creating database<----------------
# mydata=mysql.connector.connect(host="localhost",user="root",password="krish@6089")
# my_cur=mydata.cursor()
# q1="create database railway"
# my_cur.execute(q1)


#-------->creating table called Train details who contains the time table of the train<------------------
mydata=mysql.connector.connect(host="localhost",user="root",password="krish@6089",database="railway")
my_cur=mydata.cursor()
# q1="create table traindetails(T_name VARCHAR(30) not null,T_no VARCHAR(6) primary key,start_station VARCHAR(25)not null,end_station VARCHAR(25)not null,S_time TIME not null,R_time TIME not null,platform_no int(2)not null)"
# my_cur.execute(q1)

#-------->inserting the data of 25 train in the table<-----------------
# mydata=mysql.connector.connect(host="localhost",user="root",password="krish@6089",database="railway")
# my_cur=mydata.cursor()
# insert_query = """
#         INSERT INTO traindetails (T_name, T_no, start_station, end_station, S_time, R_time, platform_no)
#         VALUES (%s, %s, %s, %s, %s, %s, %s)
# """
# train_data = [
#             ('Rajdhani Express', 12951, 'Delhi', 'Mumbai', '20:10:00', '07:30:00', 5),
#             ('Duronto Express', 12268, 'Bangalore', 'Delhi', '23:50:00', '05:30:00', 2),
#             ('Jan Shatabdi', 12023, 'Patna', 'Ranchi', '16:10:00', '19:40:00', 3),
#             ('Garib Rath', 12910, 'Chennai', 'Mumbai', '22:40:00', '09:20:00', 4),
#             ('Humsafar Express', 22867, 'Kolkata', 'Bangalore', '19:55:00', '10:45:00', 6),
#             ('Deccan Queen', 12124, 'Pune', 'Mumbai', '07:00:00', '10:25:00', 7),
#             ('Intercity Express', 12627, 'Bangalore', 'Chennai', '05:20:00', '10:10:00', 8),
#             ('Gatimaan Express', 12049, 'Delhi', 'Agra', '08:10:00', '09:50:00', 9),
#             ('Tejas Express', 22120, 'Goa', 'Mumbai', '10:00:00', '19:30:00', 10),
#             ('Satavahana Express', 12713, 'Vijayawada', 'Hyderabad', '14:30:00', '19:20:00', 11),
#             ('Amritsar Express', 11057, 'Mumbai', 'Amritsar', '23:30:00', '11:30:00', 12),
#             ('Karnavati Express', 12934, 'Ahmedabad', 'Mumbai', '05:00:00', '10:10:00', 13),
#             ('Avadh Express', 19037, 'Gorakhpur', 'Bandra', '15:30:00', '20:20:00', 14),
#             ('Swarna Jayanti', 12983, 'Delhi', 'Thiruvananthapuram', '08:10:00', '19:30:00', 15),
#             ('Janshatabdi Express', 12052, 'Goa', 'Mumbai', '14:15:00', '21:15:00', 16),
#             ('Poorva Express', 12303, 'Howrah', 'New Delhi', '08:15:00', '06:05:00', 17),
#             ('Nanda Devi Express', 12401, 'New Delhi', 'Dehradun', '23:50:00', '06:10:00', 18),
#             ('Mysore Express', 16231, 'Chennai', 'Mysore', '06:15:00', '14:10:00', 19),
#             ('Howrah Mail', 12810, 'Mumbai', 'Howrah', '20:15:00', '03:50:00', 20),
#             ('Mandovi Express', 10104, 'Goa', 'Mumbai', '07:00:00', '18:45:00', 21),
#             ('Bhopal Shatabdi', 12002, 'Bhopal', 'Delhi', '15:00:00', '22:30:00', 22),
#             ('Gujarat Mail', 12902, 'Ahmedabad', 'Mumbai', '21:30:00', '06:10:00', 23),
#             ('Punjab Mail', 12138, 'Firozpur', 'Mumbai', '21:40:00', '07:35:00', 24),
#             ('Mewar Express', 12964, 'Udaipur', 'Delhi', '19:15:00', '06:30:00', 25)
#         ]

# my_cur.executemany(insert_query,train_data)
# mydata.commit()
From = input("Enter city name from you start your journy :")
From = From.capitalize()
To = input("Enter city name where you end your journy :")
To = To.capitalize()
sqlect_t_table="select * from traindetails where start_station= %s AND end_station= %s"
my_cur.execute(sqlect_t_table, (From,To))
train_table=my_cur.fetchall()
df=pd.DataFrame(train_table)
df.columns=['T_name', 'T_no','start_station', 'end_station', 'S_time', 'R_time', 'platform_no']
print(df.to_string(index=False))

# ---------------->making booking table whose connected with the  train table
# mydata=mysql.connector.connect(host="localhost",user="root",password="krish@6089",database="railway")
# my_cur=mydata.cursor()