### Menu Driven Program ###
Menu = []
choice = 0
while(choice != 7):
    print("1.Add Items")
    print("2.Remove Items")
    print("3.Print Items")
    print("4.Total Bill")
    print("5.Update Quantity of Item")
    print("6.Update Price of Item")
    print("7.Exit")
    choice = int(input("Enter your choice :"))
    if choice == 1:
        n = int(input("Enter Number of Items to Buy :"))
        for i in range(n):
            itemname = input("Enter The Name of Product :")
            itemprice = int(input("Enter the Price of Product :"))
            itemquantity = int(input("Enter the Quantity of Product :"))
            sublist = [itemname, itemprice, itemquantity]
            Menu.append(sublist)
    elif choice == 2:
        ans = input("Do you want to remove Item type (Yes) or (Y) ")
        if ans == 'Yes' or 'Y':
            itemname = input("Enter the Item name to Remove :")
            for i in range(n):
                sublist = Menu[i]
                if itemname in sublist:
                    Menu.remove(sublist)
                    print("Item Has Been Removed Succesfully !!!")
                    print(Menu)
                else:
                    pass
        elif ans == 'No' or 'N':
            pass

    elif choice == 3:
        for i in range(len(Menu)):
            print(Menu[i][0], Menu[i][1], Menu[i][2])
    elif choice == 4:
        bill=0
        for i in range (len(Menu)):
            bill=bill+Menu[i] [1] * Menu[i] [2]
        print("The Bill is :" ,bill)
    elif choice == 5:
        newbill=0
        oldname = input("Enter the itemname (Quantity) is to replace :")
        for i in range (len(Menu)):
            sublist=Menu[i]
            if oldname in sublist:
                Menu [i] [2] =int(input("Enter the New (Quantity) :"))
                print("Quantity Replaced Successfully !!!")
                print(Menu)
            
            else:
                pass
        
                break
    elif choice == 6:
        oldname = input("Enter the itemname (Price) is to replace :")
        for i in range (len(Menu)):
            sublist=Menu[i]
            if oldname in sublist:
                Menu [i] [1] =int(input("Enter the New (Price) :"))
                print("Price Replaced Successfully !!!")
                print(Menu)
        
            else:
                pass
        
    elif choice == 7:
        print("ThankYou !!!")
        
        
            
