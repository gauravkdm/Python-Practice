class Programmer :
    
    def __init__(self,name,experience , education,salary ,typeofprogrammer):
        self.name=name
        self.experience=experience
        self.education=education
        self.salary=salary
        self.typeofprogrammer=typeofprogrammer
    def  put(self):
        print("The Name of programmer is :",self.name)
        print("Exerience of programmer is :",self.experience)
        print("Education of programmer is :",self.education)
        print("Type of programmer is :",self.typeofprogrammer)
hacker=Programmer("Erichto","5years","Oxford University BTech","10lakh","Advanced Programmer")
hacker.put()
    