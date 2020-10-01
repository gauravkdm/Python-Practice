filename=input("Enter mobile number of customer :\n")
filehandler=open(filename+".txt",'r')
filedata=filehandler.read()
filehandler.close()
grocery={ }
lines=filedata.split("\n")
for line in lines :
    tempdata=line.split(",")
    grocery[tempdata[0]]={"qty":int(tempdata[1]),"price":int(tempdata[2])}
print(grocery)
total=0
for item in grocery:
    total=total+grocery[item]["qty"]*grocery[item]["price"]
print("Hello Customer , you total bill i s: \n",total)
            