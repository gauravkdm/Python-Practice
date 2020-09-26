grocery=[]
choice=0
while(choice!=5):
  print("1.Add items ")
  print("2.Print Items ")
  print("3.Total Bill ")
  print("4.Remove item ")
  print("5.Replace Price ")
  print("6.Exit")
  choice=int(input("Enter your choice :"))
  if choice==1:
      n=int(input("How many groceries items to buy :"))
      for i in range(n):
          itemname=input("Enter the name of product :")
          itemprice=int(input("Enter the price of product :"))
          sublist=[itemname,itemprice]
          grocery.append(sublist)
         
  elif choice==2:
      for i in range(len(grocery)):
          print(grocery[i][0],grocery[i][1])
  elif choice ==3:
      bill=0
      for i in range(len(grocery)):
          bill= bill + grocery[i] [1]
      print("Total Bill is :",bill)

  elif choice==4:
      for i in range (len(grocery)):
          sublist=grocery[i]
          if itemname in sublist:
              grocery.remove(sublist)
              print("Item remove sublist :")
              print(grocery)
              break
          else:
              pass
  elif choice==5:
     oldname=input("Enter the item name price is to replace :")
     for i in range(len(grocery)):
         sublist=grocery[i]
         if oldname in sublist:
             grocery[i] [1]=int(input("Enter new price :"))
             print(grocery)
             newbill=0
             for i in range(len(grocery)):
                 newbill=newbill +grocery[i] [1]

             print("New Bill is :",newbill )

  elif choice==6:
      print("Thankyou :) ")


    
