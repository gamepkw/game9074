import pickle

import os

import pathlib

import mysql.connector


class Account :

   accNo = 0

   name = ""

   deposit=0

   type = ""

   def createAccount(self):

       self.accNo= int(input("Enter the account no : "))

       self.name = input("Enter the account holder name : ")

       self.type = input("Enter the type of account [C/S] : ")

       self.deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current : "))
       
       print("\n\n\nAccount Created")
   
   a = accNo
   b = name
   c = type
   
   print(a,b,c)
   def insert_varibles_into_table(accNo,name,type):
    connection = mysql.connector.connect(
        
    host="localhost",
    user="root",
    passwd="1234",
    database='banking')
    
    cursor = connection.cursor()
    mySql_insert_query = """INSERT INTO account (accountNo, holderName, accountType) 
                                VALUES (accNo, name, type) """

    record = (accNo, name, type)
    cursor.execute(mySql_insert_query, record)
    connection.commit()
    print("successfully")
   

       

def intro():

   print("\t\t\t\t**********************")

   print("\t\t\t\tBANK MANAGEMENT SYSTEM")

   print("\t\t\t\t**********************")

   print("\t\t\t\tBrought To You By:")

   print("\t\t\t\tprojectworlds.in")

   input()

def writeAccount():

   account = Account()

   account.createAccount()

   writeAccountsFile(account)
   
   
   



def writeAccountsFile(account) :  

   file = pathlib.Path("accounts.data")

   if file.exists ():

       infile = open('accounts.data','rb')

       oldlist = pickle.load(infile)

       oldlist.append(account)

       infile.close()

       os.remove('accounts.data')

   else :

       oldlist = [account]

   outfile = open('newaccounts.data','wb')

   pickle.dump(oldlist, outfile)

   outfile.close()

   os.rename('newaccounts.data', 'accounts.data')      

# start of the program

ch= ""

num=0

intro()

while ch != 8:

   #system("cls");

   print("\tMAIN MENU")

   print("\t1. NEW ACCOUNT")

   ch = input()

   #system("cls");  

   if ch == '1':

       writeAccount()

   elif ch =='2':

       num = int(input("\tEnter The account No. : "))

       depositAndWithdraw(num, 1)

   elif ch == '3':

       num = int(input("\tEnter The account No. : "))

       depositAndWithdraw(num, 2)

   elif ch == '4':

       num = int(input("\tEnter The account No. : "))

       displaySp(num)

   elif ch == '5':

       displayAll();

   elif ch == '6':

       num =int(input("\tEnter The account No. : "))

       deleteAccount(num)

   elif ch == '7':

       num = int(input("\tEnter The account No. : "))

       modifyAccount(num)

   elif ch == '8':

       print("\tThanks for using bank management system")

       break

   else :

       print("Invalid choice")  

   ch = input("Enter your choice : ")  
   
   
   
   
   
   "--------------------------------------------"
   "Database"


