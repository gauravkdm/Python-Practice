class pen:
    ink_status="None"
    ink_color="None"
    size="None"
    shape="None"
    manufacturer="None"
    
    def create_pen(self):
        self.ink_status=input("Does the pen has ink in it :")
        self.ink_color=input("What color ink do you want to filled in it :")
        self.size=input("What is the pen size : [in cms] :")
        self.shape=input("What is the pen shape/design :")
        self.manufacturer=input("Which company manufacturer the pen is :")
    def view_pen (self):
        print("The pen ink status is :",self.ink_status )
        print("The pen ink color is :",self.ink_color)
        print("The size of pen is :",self.size)
        print("The shape of pen is :",self.shape)
        print("This pen ink manufacturer is :",self.manufacturer )
        