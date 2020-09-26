grocery=[]
choice=0
while(choice!=3):
  print("1.Add items ")
  print("2.Print Items")
  print("3.Replace Items")
  print("4.Remove Items")
  print("5.Insert Items")
  print("6.View Price")
  print("6.Exit")
  choice=int(input("Enter your choice :"))
  if choice==1:
    n=int(input("How many groceries items to buy "))
    for i in range(n):
      itemname=input("Enter the name of product")
      grocery.append(itemname)
  elif (choice==2):
    print(grocery)
  elif (choice==3):
    olditem=input("which item do you want to repalce")
    pos=grocery.index(olditem)
    grocery[pos]=input("Enter the new item")
    print(grocery)
  elif(choice==4):
    itemname=input("which item to be remove")
    if itemname in grocery :
      grocery.remove(itemname)
    else:
      print(itemname,"does not exist in the list")
    print(grocery)
  elif choice==5:
    itemname=input("Enter the name to insert the product")
    pos=int(input("Enter the position to insert at "))
    grocery.insert(pos,itemname)
  else:
    pass  
    
   


