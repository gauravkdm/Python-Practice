from g1 import pen
pens=[]
n=int(input("How many pens to create :"))
for i in range (n):
    p1=pen()
    p1.create_pen()
for i in range(n):
    p1.view_pen()
    