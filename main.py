# import traintable
# import passengersdetails
import mysql.connector
import pandas as pd
import random

print("Welcome to the Railway Reservation system")
print("chhose a number as your need")
print("1.To show the time table of train and book the seat :")
print("2.To cancel your seat:")
print("3.To Exit:")
ch=1
while ch >=1 and ch <=2:
    ch=int(input("Enter your choice as you need :"))
    print(f"your chooice is :{ch}")
    if ch == 1:
        mydata=mysql.connector.connect(host="localhost",user="root",password="krish@6089",database="railway")
        my_cur=mydata.cursor()
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
        print("-"*50)
        ask=input("Do you want to book your seat ?")
        if ask =="yes" or ask =="YES" or ask == "Yes":
            p_name=input("Enter your Full name : ")
            p_name = p_name.capitalize()
            p_age = int(input("Enter Your Age : "))
            T_name=input("Enter Train name :")
            T_name = T_name.capitalize()
            T_no=int(input("Enter the number of Train : "))
            pnr=random.randint(10000000000,999999999999)
            start_station=input("Enter your starting station name : ")
            start_station = start_station.capitalize()
            end_station=input("Enter your ending station name : ")
            end_station = end_station.capitalize()
            print("select comartment !")
            print("1.AC1 THE charge of it is INR 2000:")
            print("2.AC2 THE charge of it is INR 1700:")
            print("3.AC3 THE charge of it is INR 1500:")
            print("4.sleeper THE charge of it is INR 1200:")
            print("5.second sleaper THE charge of it is INR 900:")
            print("6.sitting THE charge of it is INR 650:")
            print("7.general THE charge of it is INR 450:")
            compartment=int(input("Enter your comartment number :"))
            payment = int(input("Enter your upi id :"))
            print("The money is successfully debit from your upi. ")
            print(F"Hi {p_name} ! your seat is booked in {T_name} {T_no} and your pnr is: {pnr}")
            mydata=mysql.connector.connect(host="localhost",user="root",password="krish@6089",database="railway")
            my_cur=mydata.cursor()
            insert_query = """
            INSERT INTO passengers (p_name, p_age, T_name, T_no,pnr,compartment, start_station, end_station, payment)
            VALUES (%s, %s, %s, %s, %s, %s, %s ,%s ,%s) """
            Value=(p_name,p_age,T_name,T_no,pnr,compartment,start_station,end_station,payment)
            my_cur.execute(insert_query,Value)
            mydata.commit()
            listpnr=[pnr]
            ask=input("Do you Wnt to See your details ?")
            if ask =="yes" or ask =="YES" or ask == "Yes":
                selectdetails="select * from passengers where pnr = %s"
                my_cur.execute(selectdetails,(listpnr))
                showingdetails = my_cur.fetchall()
                if showingdetails:
                    print("your booking status :")
                    print("-"*50)
                    for row in showingdetails:
                        print(f"Passenger Name :{row[0]}, Passenger Age :{row[1]}, Train name :{row[2]}, Train no :{row[3]} ")
                        print(f"Passenger PNR :{row[4]},compartment number :{row[5]}, start station :{row[6]}, End station :{row[7]}, Payment :{row[8]} ")
                    print("-"*50)
                else:
                    print(f"There is no passenger details found on this {pnr}")
            else:
                enterch =2
                
        print("Do you Want to exit? 1 for no 2 for yes")
        enterch=int(input("Enter your choice"))
        if enterch == 1:
            print("Welcome to the Railway Reservation system")
            print("chhose a number as your need")
            print("1.To show the time table of train and book the seat :")
            print("2.To cancel your seat:")
            print("3.To Exit:")




                


    elif ch ==2:
        pnr1=input("Enter Your pnr ro cancel : ")
        pnr1=[pnr1]
        mydata=mysql.connector.connect(host="localhost",user="root",password="krish@6089",database="railway")
        my_cur=mydata.cursor()
        def cancel_booking(pnr1):
            selectquery="select * from passengers where pnr = %s"
            my_cur.execute(selectquery,(pnr1))
            record=my_cur.fetchone()

            if record:
                delquery="delete from passengers where pnr = %s"
                my_cur.execute(delquery,(pnr1))
                mydata.commit()
                print(f"Record With {pnr1} has been deleted")
                print("chhose a number as your need")
                print("1.To show the time table of train and book the seat :")
                print("2.To cancel your seat:")
                print("3.To Exit:")

            else:
                print("Enter right pnr number!....")
        cancel_booking(pnr1)
        my_cur.close()
        mydata.close()
        







    