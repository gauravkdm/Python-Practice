choice=0
while(choice!=3):
    print("1.Email Address")
    print("2.Username")
    print("3.Exit")
    choice=int(input("Enter the choice "))
    if choice==1:
        name=input("Enter your First Name :")
        lastname=input("Enter your last name :")
        mob=input("Enter your mobile number")
        namefirst=name[0].upper() + name[1:]
        lastfirst=lastname[0].upper() + lastname[1:]
        Email=namefirst +"."+ lastfirst + "@gmail.com"
        print(Email)
    elif choice ==2:
        namefi=name[0:2]
        lastfi=lastname[0:2]
        username=namefi + lastfi + mob[0:2] + mob[-2:]
        print(username)
    elif choice ==3:
        print("thankyou")
         
   

    
 