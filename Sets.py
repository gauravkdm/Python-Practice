set1=set()
set2=set()
choice=0
while(choice!=7):
    print("1.Add elements in sets")
    print("2.Remove elements in sets")
    print("3.Union ")
    print("4.Intersection")
    print("5.Difference")
    print("6.Symmetrical Sets")
    print("7.Exit")
    choice= int(input("enter your choice"))
    
    if choice==1:
        n= int(input("Enter the no of elements in set 1 :"))
        for i in range(n):
            inputs1=int(input("Enter the Elements of set1"))
            set1.add(inputs1)
        print(set1)
        n1= int(input("Enter the no of elements in set 2 :"))
        for i in range(n1):
            inputs2=int(input("Enter the Elements of set1"))
            set2.add(inputs2)
        print(set2)
    elif choice ==2:
        whichset=input("Enter the name of set elements to be remove")
        if whichset == "set1":
            whichelement=int(input("Enter the value to remove from set 1 :"))
            if whichelement in set1:
                set1.remove(whichelement)
                print(set1)
        elif whichset =="set2":
            whichelement=int(input("Enter the value to remove from set 2 : "))
            if whichelement in set2:
                set2.remove(whichelement1)
                print(set2)
    elif choice==3:
        unionset=set1.union(set2)
        print(unionset)
    elif choice==4:
        interset=set1.intersection(set2)
        print(interset)
    elif choice==5:
        diff1=set1.difference(set2)
        diff2=set2.difference(set1)
        print(diff1)
        print(diff2)
    elif choice==6:
        seti=set1.symmetric_difference(set2)
        print(seti)
    elif choice==7:
        print("Thankyou")
                
        
            
    