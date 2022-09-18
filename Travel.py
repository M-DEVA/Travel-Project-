
import mysql.connector

connection = mysql.connector.connect(

    host="localhost",
    user="root",
    password="12345",
    database="Travel"
)

print("***********\nwelcome to UNDERTAKER TRAVEL AGENCY**************")
            
        
fromaddress = ""
toaddress = ""
members = ""
myname = ""
days = ""

name = input("\nEnter your Name :")

fromlocation = input("\nEnter your From Location :")
        
to = (input("\nEnter TO Location :"))

YourDays = input("\nEnter your Days :")

days = YourDays

myname = name 

fromaddress = fromlocation
toaddress = to


val = (myname,fromaddress,toaddress,members,days)

sql = "INSERT INTO details(my_name, from_address, to_address, mem_bers ,Your_Days) VALUES (%s, %s, %s, %s, %s )"
mycursor = connection.cursor()

mycursor.execute(sql,val)
connection.commit()

print("\nSelect your option")

print("1. 3 Members and 20000 budject")

print("2. 5 Members and 30000 budject")

print("3. 7 Members and 50000 budject")



def option1(howmanymembers,your_budjet):

    if howmanymembers<=3:

        if your_budjet <=20000:

            print("\nyour amount is 20000")

            print("\nYour Members 3 and Budject is 20000")
            
            print("\nHappy to travel...")
    
    else:    

        print("\nOnly 3 members & 20000 allowed this option")

        print("\nAbove 3 choose oter option")    

def option2(howmanymembers,your_budjet):

    if howmanymembers<=5:

        if your_budjet <=30000:
        
            print("\nyour amount is 30000")

            print("\nYour Members 5 and Budject is 30000")
        
            print("\nHappy to travel...")
    
    else:    

        print("\nOnly 5 members & 30000 allowed this option")

        print("\nAbove 5 choose oter option")     

def option3(howmanymembers,your_budjet):

    if howmanymembers<=7:

        if your_budjet <=50000:

            print("\nyour amount is 50000")

            print("\nYour Members 7 and Budject is 50000")
            
            print("\nHappy to travel...")
    
    else:    

        print("\nOnly 7 members & 50000 allowed this option")

        print("\nAbove 5 choose oter option") 


user=int(input("\nEnter your number:"))



if user==1:
    print("\nEnter to how many member to going... ")

    howmanymembers =int(input("\nEnter to Going members:"))

    members = howmanymembers 

    your_budjet=int(input("\nEnter your budjet:"))

    option1(howmanymembers,your_budjet)

    members = howmanymembers
    fromaddress = fromlocation
    toaddress = to
    val = (myname,fromaddress,toaddress,members,days)

    sql = "INSERT INTO details(my_name, from_address, to_address, mem_bers ,Your_Days) VALUES (%s, %s, %s, %s, %s )"
    mycursor = connection.cursor()

    mycursor.execute(sql,val)
    connection.commit()


if user==2:
    print("\nEnter to how many member to going... ")

    howmanymembers =int(input("\nEnter to Going members:"))

    members = howmanymembers 

    your_budjet=int(input("\nEnter your budjet:"))

    option2(howmanymembers,your_budjet)

    members = howmanymembers
    fromaddress = fromlocation
    toaddress = to
    val = (myname,fromaddress,toaddress,members,days)

    sql = "INSERT INTO details(my_name, from_address, to_address, mem_bers ,Your_Days) VALUES (%s, %s, %s, %s, %s )"
    mycursor = connection.cursor()

    mycursor.execute(sql,val)
    connection.commit()


if user==3:
    print("\nEnter to how many member to going... ")

    howmanymembers =int(input("\nEnter Going members:"))

    members = howmanymembers 

    your_budjet=int(input("\nEnter your budjet:"))

    option3(howmanymembers,your_budjet)

    members = howmanymembers
    fromaddress = fromlocation
    toaddress = to
    val = (myname,fromaddress,toaddress,members,days)

    sql = "INSERT INTO details(my_name, from_address, to_address, mem_bers ,Your_Days) VALUES (%s, %s, %s, %s, %s )"
    mycursor = connection.cursor()

    mycursor.execute(sql,val)
    connection.commit() 
print("********Happy and Safe Journey*********")           
connection.commit() 
    