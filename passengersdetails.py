import mysql.connector

mydata=mysql.connector.connect(host="localhost",user="root",password="krish@6089",database="railway")
my_cur=mydata.cursor()
q1="create table passengers(p_name varchar(25) not null, p_age int not null,T_name VARCHAR(30) not null references traindetails(T_name),T_no VARCHAR(30) not null references traindetails(T_no),pnr varchar(12) not null ,compartment int(1) not null,start_station VARCHAR(30) not null references traindetails(start_station),end_station VARCHAR(30) not null references traindetails(end_station),payment varchar(12))"
my_cur.execute(q1)
# q1="drop table passengers"
# my_cur.execute(q1)

