#imposting important modules and connecting with mysql
import csv
import mysql.connector as m
con=m.connect(host='localhost', user='root', passwd='0000',database='lib')

#to use this file for first time, call function create_userfile() and make sure abt database being empty.
#Keep font size as 8

# to start with the program

print("{:=^215}".format("  WELCOME TO LIBRARY MANAGEMENT SYSTEM  "))
    
def create_book():
    #To create the Main table Book
    
    cursor=con.cursor()
    cursor.execute('''create table BOOK (B_Id integer primary key, Name char(60), Category char(20), Summary varchar(200), PPD integer, price integer);''')

def insert_book():
    #To insert records in the main table Book
    
    cursor=con.cursor()
    cursor.execute('''insert into BOOK values(001,
    "The Lord of the Rings Part1",
    "fantasy",
    "the saga of a group of sometimes reluctant heroes who set forth to save their world from consummate evil",
    40,
    500)''') 
    con.commit()
    
    cursor.execute('''insert into BOOK values(002,
    "Dune",
    "sci-fi",
    "fictional story set in a space empire far in the future",
    35,
    400)''') 
    con.commit()
    
    cursor.execute('''insert into BOOK values(003,
    "Murder on the Orient Express",
    "mystery",
    "A group of passengers trapped on the Orient Express in a snow storm with a murdered body and a Belgian detective to keep them company",
    20,
    300)''') 
    con.commit()
    
    cursor.execute('''insert into BOOK values(004,
    "Nineteen Eighty-four",
    "sci-fi",
    "a low ranking member of 'the Party', who is frustrated by the omnipresent eyes of the party, and its ominous ruler Big Brother",
    25,
    350)''') 
    con.commit()
    
    cursor.execute('''insert into BOOK values(005,
    "Pride and Prejudice",
    "romance",
    "the turbulent relationship between Elizabeth Bennet, the daughter of a country gentleman, and Fitzwilliam Darcy, a rich aristocratic landowner.",
    20,
    300)''') 
    con.commit()
    
    cursor.execute('''insert into BOOK values(006,
    "American Gods",
    "contemporary",
    "explores the expedition of Shadow, an ex-convict and the mysterious Mr Wednesday",
    30,
    400)''') 
    con.commit()
    
    cursor.execute('''insert into BOOK values(007,
    "The God of Small Things",
    "indian",
    "the childhood experiences of fraternal twins whose lives are destroyed by the 'Love Laws' that lay down 'who should be loved, and how. And how much'",
    25,
    350)''') 
    con.commit()
    
    cursor.execute('''insert into BOOK values(008,
    "A suitable boy",
    "contemporary",
    "Modernity confronts tradition in post-Partition India as a young student resists an arranged marriage and a politician's son has a transgressive affair",
    30,
    400)''') 
    con.commit()
    
    cursor.execute('''insert into BOOK values(009,
    "The Hobbit",
    "fantasy",
    "follows the quest of home-loving Bilbo Baggins, the titular hobbit, to win a share of the treasure guarded by Smaug the dragon.",
    40,
    500)''') 
    con.commit()
    
    cursor.execute('''insert into BOOK values(010,
    "A Silent Patient",
    "mystery",
    "a shocking psychological thriller of a woman's act of violence against her husband—and of the therapist obsessed with uncovering her motive.",
    35,
    400)''') 
    con.commit()
    
    cursor.execute('''insert into BOOK values(011,
    "Malgudi Days",
    "indian",
    "32 stories, all set in the fictional town of Malgudi, located in South India.",
    40,
    500)''') 
    con.commit()
    
    cursor.execute('''insert into BOOK values(012,
    "The outlander",
    "romance",
    "nurse Claire Randall, who travels through time to 18th century Scotland and finds adventure and romance with the dashing Jamie Fraser",
    30,
    400)''') 
    con.commit()
    
    cursor.execute('''insert into BOOK values(013,
    "The wedding date",
    "romance",
    "A groomsman and his last-minute guest are about to discover if a fake date can go the distance in a fun and flirty debut novel",
    30,
    400)''') 
    con.commit()
    
    cursor.execute('''insert into BOOK values(014,
    "The Left Hand of Darkness",
    "sci-fi",
    "story of Genly Ai, a human native of Terra, who is sent to the planet of Gethen as an envoy of the Ekumen, a loose confederation of planets",
    35,
    450)''') 
    con.commit()
    
    cursor.execute('''insert into BOOK values(015,
    "The Goldfinch",
    "contemporary",
    "13-year-old Theodore Decker, survives a terrorist bombing at an art museum where his mother is killed. ",
    30,
    300)''') 
    con.commit()
    
    cursor.execute('''insert into BOOK values(016,
    "Train to Pakistan",
    "indian",
    "It recounts the Partition of India in August 1947 through the perspective of Mano Majra, a fictional border village",
    35,
    350)''') 
    con.commit()
    
    #all records are inserted
    
    
def ch1(a):
    #to display order history

    #fetching details from sql
    c=con.cursor()
    s="select * from {} ".format(a)
    c.execute(s)
    d=c.fetchall()
    
    print("\n{:-^215}\n".format(" YOUR ORDER HISTORY IS "))

    #printing the input in table format

    #header
    print("+{:-^3}+{:-<30}+{:-^12}+{:-^5}+{:-^12}+{:-^5}+{:-^5}+".format("","","","","","",""))
    print("|{:^3}|{:<30}|{:^12}|{:^5}|{:^12}|{:^5}|{:^5}|".format("BID","BOOK NAME","ISSUE DATE","PPD","RETURN DATE","NOD","PRICE"))

    #table contents
    for i in d:
        print("|{:-^3}|{:-<30}|{:-^12}|{:-^5}|{:-^12}|{:-^5}|{:-^5}|".format("","","","","","",""))
        print("|{:^3}|{:<30}|{:^12}|{:^5}|{:^12}|{:^5}|{:^5}|".format(i[0],i[1],i[2],i[3],str(i[4]),str(i[5]),str(i[6])))
    print("+{:-^3}+{:-<30}+{:-^12}+{:-^5}+{:-^12}+{:-^5}+{:-^5}+".format("","","","","","",""))


def ch2():
    #to display all books

    #fetching details from sql
    c=con.cursor()
    s="select * from book"
    c.execute(s)
    d=c.fetchall()

    print("\n{:-^215}\n".format(" ALL THE BOOKS AND THEIR DETAILS ARE "))

    #printing the input in table format

    #header
    print("+{:-<3}+{:-<30}+{:-<14}+{:-<151}+{:-<4}+{:-^5}+".format("","","","","",""))
    print("|{:<3}|{:<30}|{:<14}|{:<151}|{:<4}|{:^5}|".format("BID","BOOK NAME","CATEGORY","SUMMARY","PPD","PRIZE"))

    #table contents
    for i in d:
        print("|{:-<3}|{:-<30}|{:-<14}|{:-<151}|{:-<4}|{:-^5}|".format("","","","","",""))
        print("|{:<3}|{:<30}|{:<14}|{:<151}|{:<4}|{:^5}|".format(i[0],i[1],i[2],i[3],(i[4]),(i[5])))
    print("+{:-<3}+{:-<30}+{:-<14}+{:-<151}+{:-<4}+{:-^5}+".format("","","","","",""))
    

def ch3():
    #to search books by particular category

    #fetching details from sql using given category
    c=con.cursor()
    #Asking a category
    b=input("Enter BOOK CATEGORY : ")
    s="select * from book where Category='{}' ".format(b)
    c.execute(s)
    d=c.fetchall()
    
    print("\n{:-^215}\n".format(" ALL THE BOOKS AND THEIR DETAILS FROM GIVEN CATEGORY ARE "))
    
    #printing the input in table format

    #header
    print("+{:-<3}+{:-<30}+{:-<14}+{:-<151}+{:-<4}+{:-^5}+".format("","","","","",""))
    print("|{:<3}|{:<30}|{:<14}|{:<151}|{:<4}|{:^5}|".format("BID","BOOK NAME","CATEGORY","SUMMARY","PPD","PRIZE"))

    #table contents
    for i in d:
        print("|{:-<3}|{:-<30}|{:-<14}|{:-<151}|{:-<4}|{:-^5}|".format("","","","","",""))
        print("|{:<3}|{:<30}|{:<14}|{:<151}|{:<4}|{:^5}|".format(i[0],i[1],i[2],i[3],(i[4]),(i[5])))
    print("+{:-<3}+{:-<30}+{:-<14}+{:-<151}+{:-<4}+{:-^5}+".format("","","","","",""))

    
def ch4():
    #to search books by name

    #fetching details from sql using given name
    c=con.cursor()
    b=input("Enter the NAME of the BOOK : ")
    s="select * from book where Name='{}' ".format(b)
    c.execute(s)
    d=c.fetchall()

    print("\n{:-^215}\n".format(" THE BOOK AND ITS DETAILS ARE "))
    
    #printing the input in table format

    #header
    print("+{:-<3}+{:-<30}+{:-<14}+{:-<151}+{:-<4}+{:-^5}+".format("","","","","",""))
    print("|{:<3}|{:<30}|{:<14}|{:<151}|{:<4}|{:^5}|".format("BID","BOOK NAME","CATEGORY","SUMMARY","PPD","PRIZE"))

    #table contents
    for i in d:
        print("|{:-<3}|{:-<30}|{:-<14}|{:-<151}|{:-<4}|{:-^5}|".format("","","","","",""))
        print("|{:<3}|{:<30}|{:<14}|{:<151}|{:<4}|{:^5}|".format(i[0],i[1],i[2],i[3],(i[4]),(i[5])))
    print("+{:-<3}+{:-<30}+{:-<14}+{:-<151}+{:-<4}+{:-^5}+".format("","","","","",""))


def ch5():
    #to search books by BOOK ID

    #fetching details from sql using given B ID
    c=con.cursor()
    b=int(input("Enter BOOK ID : "))
    s="select * from book where B_Id={} ".format(b)
    c.execute(s)
    d=c.fetchall()
    
    print("\n{:-^215}\n".format(" THE BOOK AND ITS DETAILS ARE "))
    
    #printing the input in table format

    #header
    print("+{:-<3}+{:-<30}+{:-<14}+{:-<151}+{:-<4}+{:-^5}+".format("","","","","",""))
    print("|{:<3}|{:<30}|{:<14}|{:<151}|{:<4}|{:^5}|".format("BID","BOOK NAME","CATEGORY","SUMMARY","PPD","PRIZE"))

    #table contents
    for i in d:
        print("|{:-<3}|{:-<30}|{:-<14}|{:-<151}|{:-<4}|{:-^5}|".format("","","","","",""))
        print("|{:<3}|{:<30}|{:<14}|{:<151}|{:<4}|{:^5}|".format(i[0],i[1],i[2],i[3],(i[4]),(i[5])))
    print("+{:-<3}+{:-<30}+{:-<14}+{:-<151}+{:-<4}+{:-^5}+".format("","","","","",""))
        

def ch6(a):
    #to issue a book using its book id
    
    #fetching details from sql using given B ID
    c=con.cursor()
    m=int(input("Enter BOOK ID : "))
    s="select * from book where B_Id={} ".format(m)
    c.execute(s)
    d=c.fetchall()

    #inserting values into the customer table
    s1="insert into {} values ('{}','{}',CURDATE(),{},default,default,default)".format(a,m,d[0][1],d[0][4])
    c.execute(s1)
    con.commit()

    print("\n{:-^215}\n".format(" THANK YOU, YOUR BOOK IS ISSUED "))

    
def ch7(a):
    #to return a book using its book id

    #fetching details from sql using given B ID
    c=con.cursor()
    m=int(input("Enter BOOK ID : "))
    s="select * from book where B_Id={} ".format(m)
    c.execute(s)
    d=c.fetchall()

    #inserting values into the customer table
    #DATE
    s1="update {} set return_date=curdate() where b_id={}".format(a,m)
    c.execute(s1)
    #NUMBER OF DAYS
    s2="update {} set no_of_days=DATEDIFF(return_date , issue_date ) where b_id={}".format(a,m)
    c.execute(s2)
    #TOTAL PRIZE
    s3="update {} set total_prize=50+ppd+ppd*no_of_days where b_id={}".format(a,m)
    c.execute(s3)
    con.commit()
    
    print("\n{:-^215}\n".format(" THANK YOU, YOUR BOOK IS RETURNED, PLEASE VIEW ORDER HISTORY TO KNOW THE TOTAL PRICE "))

        
def ch8(a):
    #to diplay the no. of books borrowed

    #fetching the details from sql
    c=con.cursor()
    s="select * from {} where return_date is NULL".format(a)
    c.execute(s)
    d=c.fetchall()
    
    print("\n{:-^215}\n".format(" BOOKS BORROWED ARE "))

    #printing the input in table format

    #header
    print("+{:-^3}+{:-<30}+{:-^12}+{:-^5}+{:-^12}+{:-^5}+{:-^5}+".format("","","","","","",""))
    print("|{:^3}|{:<30}|{:^12}|{:^5}|{:^12}|{:^5}|{:^5}|".format("BID","BOOK NAME","ISSUE DATE","PPD","RETURN DATE","NOD","PRICE"))

    #table contents
    for i in d:
        print("|{:-^3}|{:-<30}|{:-^12}|{:-^5}|{:-^12}|{:-^5}|{:-^5}|".format("","","","","","",""))
        print("|{:^3}|{:<30}|{:^12}|{:^5}|{:^12}|{:^5}|{:^5}|".format(i[0],i[1],i[2],i[3],str(i[4]),str(i[5]),str(i[6])))
    print("+{:-^3}+{:-<30}+{:-^12}+{:-^5}+{:-^12}+{:-^5}+{:-^5}+".format("","","","","","",""))

    #counting the no. of books borrowed
    s2="select count(b_id) from {} where return_date is NULL".format(a)
    c.execute(s2)
    d=c.fetchall()
    for i in d:
        print("\nTHE NUMBER OF BOOKS BORROWED ARE : ",*i)


def ch9(a):
    #to display books issued on particular date

    #fetching the details from sql using given date
    c=con.cursor()
    b=input("Enter ISSUE DATE : ")
    s="select * from {} where issue_date='{}'".format(a,b)
    c.execute(s)
    d=c.fetchall()
    
    print("\n{:-^215}\n".format(" BOOKS BORROWED ON THAT DATE ARE "))

    #printing the input in table format

    #header
    print("+{:-^3}+{:-<30}+{:-^12}+{:-^5}+{:-^12}+{:-^5}+{:-^5}+".format("","","","","","",""))
    print("|{:^3}|{:<30}|{:^12}|{:^5}|{:^12}|{:^5}|{:^5}|".format("BID","BOOK NAME","ISSUE DATE","PPD","RETURN DATE","NOD","PRICE"))

    #table contents
    for i in d:
        print("|{:-^3}|{:-<30}|{:-^12}|{:-^5}|{:-^12}|{:-^5}|{:-^5}|".format("","","","","","",""))
        print("|{:^3}|{:<30}|{:^12}|{:^5}|{:^12}|{:^5}|{:^5}|".format(i[0],i[1],i[2],i[3],str(i[4]),str(i[5]),str(i[6])))
    print("+{:-^3}+{:-<30}+{:-^12}+{:-^5}+{:-^12}+{:-^5}+{:-^5}+".format("","","","","","",""))

    #counting the no. of books borrowed on that day
    s2="select count(b_id) from {} where issue_date='{}'".format(a,b)
    c.execute(s2)
    d=c.fetchall()
    for i in d:
        print("\nTHE NUMBER OF BOOKS BORROWED THAT DAY ARE : ",*i)


def ch10(a):
    #to display books returned on particular date

    #fetching the details from sql using given date
    c=con.cursor()
    b=input("Enter RETURN DATE : ")
    s="select * from {} where return_date='{}'".format(a,b)
    s2="select count(b_id) from {} where return_date='{}'".format(a,b)
    c.execute(s)
    d=c.fetchall()
    
    print("\n{:-^215}\n".format(" BOOKS RETURNED ON THAT DATE ARE "))

    #printing the input in table format

    #header
    print("+{:-^3}+{:-<30}+{:-^12}+{:-^5}+{:-^12}+{:-^5}+{:-^5}+".format("","","","","","",""))
    print("|{:^3}|{:<30}|{:^12}|{:^5}|{:^12}|{:^5}|{:^5}|".format("BID","BOOK NAME","ISSUE DATE","PPD","RETURN DATE","NOD","PRICE"))

    #table contents
    for i in d:
        print("|{:-^3}|{:-<30}|{:-^12}|{:-^5}|{:-^12}|{:-^5}|{:-^5}|".format("","","","","","",""))
        print("|{:^3}|{:<30}|{:^12}|{:^5}|{:^12}|{:^5}|{:^5}|".format(i[0],i[1],i[2],i[3],str(i[4]),str(i[5]),str(i[6])))
    print("+{:-^3}+{:-<30}+{:-^12}+{:-^5}+{:-^12}+{:-^5}+{:-^5}+".format("","","","","","",""))

    #counting the no. of books RETURNED on that day
    s2="select count(b_id) from {} where return_date='{}'".format(a,b)
    c.execute(s2)
    d=c.fetchall()
    for i in d:
        print("\nTHE NUMBER OF BOOKS RETURNED THAT DAY ARE : ",*i)


def ch11(a):
    #to display particular book history

    #fetching the details from sql using given BOOK ID
    c=con.cursor()
    m=input("Enter BOOK ID : ")
    s="select * from {} where b_id={}".format(a,m)
    c.execute(s)
    d=c.fetchall()
    
    print("\n{:-^215}\n".format(" BOOK HISTORY IS "))
    
    #printing the input in table format

    #header
    print("+{:-^3}+{:-<30}+{:-^12}+{:-^5}+{:-^12}+{:-^5}+{:-^5}+".format("","","","","","",""))
    print("|{:^3}|{:<30}|{:^12}|{:^5}|{:^12}|{:^5}|{:^5}|".format("BID","BOOK NAME","ISSUE DATE","PPD","RETURN DATE","NOD","PRICE"))

    #table contents
    for i in d:
        print("|{:-^3}|{:-<30}|{:-^12}|{:-^5}|{:-^12}|{:-^5}|{:-^5}|".format("","","","","","",""))
        print("|{:^3}|{:<30}|{:^12}|{:^5}|{:^12}|{:^5}|{:^5}|".format(i[0],i[1],i[2],i[3],str(i[4]),str(i[5]),str(i[6])))
    print("+{:-^3}+{:-<30}+{:-^12}+{:-^5}+{:-^12}+{:-^5}+{:-^5}+".format("","","","","","",""))
        
def menu(a):
    #menu to give users choices for the function they want to perform
    
    while True:
        
        print()
        
        x=int(input("""PRESS
1-->to displsy order history
2-->to display all books
3-->to search book by category
4-->to search book by name
5-->to search book by id
6-->to issue a book
7-->to return a book
8-->to display no. of books borrowed
9-->to display books issued on particular date
10-->to to display books returned on particular date
11-->to display particular book history
0--> to logout : """))
        
        print()

        #to call functions using their choices
        
        if x==1:
            ch1(a)
            #to displsy ur order history
            
        elif x==2:
            ch2()
            #to display all books
            
        elif x==3:
            ch3()
            #to search book by category
            
        elif x==4:
            ch4()
            #to search book by name

        elif x==5:
            ch5()
            #to search book by id
            
        elif x==6:
            ch6(a)
            #to issue a book
            
        elif x==7:
            ch7(a)
            #to return a book
            
        elif x==8:
            ch8(a)
            #to display no. of books borrowed
            
        elif x==9:
            ch9(a)
            #to display books issued on particular date
            
        elif x==10:
            ch10(a)
            #to to display books returned on particular date
            
        elif x==11:
            ch11(a)
            #to display particular book history
            
        elif x==0:
            break
            #ending the loop
    
        else:
            print("Wrong choice entered! PLEASE TRY AGAIN")
            
        print("{:_^215}".format(""))


def create_table(a):
    #to create table for a new user
    
    c=con.cursor()
    s="""create table {}(
b_id int,
name varchar(50),
issue_date varchar(50),
ppd int,
return_date varchar(50),
no_of_days int,
total_prize int)""".format(a)
    c.execute(s)

    
def create_userfile():
    #to call this function only when u want to reboot the whole system
    
    #first drop the database and create it again

    #creating csv file
    a=open('l_users.csv','w',newline='')
    b=csv.writer(a)
    b.writerow(['username','password'])
    b.writerow(['book','admin'])

    #creating main table
    create_book()
    insert_book()
    

def sign_in():
    #signing in for new users

    #using csv to store information
    a=open('l_users.csv','r')
    p=open('l_users.csv','a',newline='')
    q=csv.writer(p)
    b=csv.reader(a)

    #letting them choose their own username
    while True:
        x=input("\nEnter USERNAME you want : ")
        for i in b:
            if x.lower()==i[0].lower():
                print("\nUsername already taken. Please try again.")
                break
        else:
            print("\nUSERNAME ALLOTTED")
            break

    #letting them choose their own password
    while True:
        y=input("\nEnter a PASSOWRD : ")
        z=input("\nConfirm PASSWORD : ")
        if y==z:
            print("\nPASSWORD CONFIRMED")
            q.writerow([x,y])
            print("\n{:-^215}".format("SUCCESFULLY SIGNED IN"))
            create_table(x)
            #x is username of the user and also its table name to be used as "a" throught the program
            break
        else:
            print("\nPasswords dont match, please try again")

    #closing the files and saving the information
    p.close()
    a.close()


def log_in():
    #to log in to the system

    #fetching details from csv file
    a=open('l_users.csv','r')
    b=csv.reader(a)

    #asking username and checking if password is correct to successfully log in
    x=input("\nEnter USERNAME : ")
    
    for i in b:
        if x==i[0]:
            while True:
                y=input("\nEnter PASSWORD : ")
                if y==i[1]:
                    print("\n{:-^215}".format(" YOU ARE NOW LOGGED IN "))
                    menu(x)
                    #x is username of the user and also its table name to be used as "a" throught the program
                    break
                else:
                    print("\nWrong password.. Please try again. " )
            break
    else:
        print("\nUsername doesnt match")
        p=int(input("""\nPRESS
1-->Log in
2-->Sign in
0-->Exit : """))
        if p==1:
            log_in()
        elif p==2:
            sign_in()
        else:
            return None

#create_userfile()

#MAIN
        
while True:
    x=int(input("""\nPRESS
1-->Log in
2-->Sign in
0-->Exit : """))
    
    if x==1:
        log_in()
        
    elif x==2:
        sign_in()
        
    elif x==0:
         break
        
    else:
        print("\nWrong choice entered! PLEASE TRY AGAIN")

#ENDING
        
print("\n{:=^215}".format("  THANK YOU. PLEASE COME AGAIN  "))

#closing the connection with sql
con.close()

#to use this file for first time, call function create_userfile() and make sure abt database being empty. Keep font size as 8
