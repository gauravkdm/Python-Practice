class pen:
    ink_status
    ink_color
    size
    shape
    manufacturer
    
    def create pen(self,i_s,i_c,si,sp,mn):
        self.inkstatus=input("Does the pen has ink in it :")
        self.ink_color=input("What color ink do you want to filled in it :")
        self.size=input("What is the pen size : [in cms] :")
        self.shape=input("What is the pen shape/design :")
        self.manufacturer=input("Which company manufacturer the pen is :")
    def view_pen (self):
        print("The pen ink status is :",self.inkstatus)
        print("The pen ink color is :",self.ink_color)
        print("The size of pen is :",self.size)
        print("The shape of pen is :",self.shape)
        print("This pen ink manufacturer is :",self.manufacturer )
        