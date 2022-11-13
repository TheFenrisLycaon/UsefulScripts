import mysql.connector
import os
import platform

mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="Shefali123@", database="eventmanagement"
)
mycursor = mydb.cursor()
c = 3


def eventsmenu():
    print("Event Management ")
    print("1. Add Event Details")
    print("2. Add Event Equipment Details")
    print("3. Book Your Event")
    print("4. Cancel Your Event")
    print("5. Quit")
    n = int(input("Enter your choice ::"))
    if n == 1:
        eventdetail()
    elif n == 2:
        equipment()
    elif n == 3:
        book()
    elif n == 4:
        print("Thank you")
    else:
        print("wrong choice")


def eventdetail():
    print("Enter Event Details")
    ch = "y"
    while ch == "y":
        l = []
        event_name = input("Enter the event name : ")
        l.append(event_name)
        event_type = input("Enter the event type : ")
        l.append(event_type)
        event_location = input("Enter the location of event: ")
        l.append(event_location)
        event_theme = input("Enter the theme of event :  ")
        l.append(event_theme)
        start_time = input("Enter the start time of event :  ")
        l.append(start_time)
        interval = input("Enter the interval between event :  ")
        l.append(interval)
        end_time = input(" Enter the end time :  ")
        l.append(end_time)
        events = l
        sql = "insert into event(event_name,event_type,event_location,event_theme,start_time,interval,end_time)values(%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql, events)
        mydb.commit()
        print("Event Details inserted successfully")
        print("Do you want to insert more Event Detail")
        ch = input("Enter yes/no ")
        print("\n" * 10)
        print("===================================================================")


def equipment():
    print("Enter Equipments Details")
    ch = "y"
    while ch == "y":
        l = []
        equipment_name = input("Enter the equipment name : ")
        l.append(equipment_name)
        equipment_type = input("Enter the equipment type : ")
        l.append(equipment_type)
        availbility = input("Enter the availblity of the equipment: ")
        l.append(availbility)
        cost = input("Enter the cost of the equipment:  ")
        l.append(cost)
        equipment = l
        sql = "insert into event_equipments(equipment_name,equipment_type,availbility,cost)values(%s,%s,%s,%s)"
        mycursor.execute(sql, equipment)
        mydb.commit()
        print("Event Equipment Details inserted successfully")
        print("Do you want to insert more Equipment Detail")
        ch = input("Enter yes/no ")
        print("\n" * 10)
        print("===================================================================")


eventsmenu()


def book():
    l = []
    cust_no = cust_no + 1
    l.append(cust_no)
    name = input("Enter the name of the customer : ")
    l.append(name)
    event_book = input("Enter the type of event you want to book : ")
    l.append(event_book)
    price = int(input("Enter the price paid for the event : "))
    l.append(price)
    cust = l
    sql = "insert into customer(cust_no,cust_name,event_book,price)values(%s,%s,%s%s)"
    mycursor.execute(sql, equipment)
    mydb.commit()
    print("Event booked successfully")
    print("Do you want to book more  events")
    ch = input("Enter yes/no ")
    print("\n" * 10)
    print("===================================================================")


eventsmenu()
