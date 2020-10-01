filename=input("Enter customer mobile number :\n")
strdata=""
n=int(input("How many products you have to purchase"))
for i in range(n):
    itemname=input("Enter product name :\n")
    itemqty=input("Enter product quantity :\n")
    itemprice=input("Enter product price :\n")
    strdata=strdata+itemname + ',' + itemqty + ',' + itemprice
    if (i<n-1):
        strdata=strdata+'\n'
filehandler=open(filename+".txt","w")
filehandler.write(strdata)
filehandler.close()