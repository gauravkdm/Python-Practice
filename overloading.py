class pen:
    inkcolor=""
    company=""
    size=""
    shape=""
    def create_pen(self,ink="blue",comp="parker",sz="",sh=""):
        self.inkcolor=ink
        self.company=comp
        self.size=sz
        self.shape=sh
    def view_pen(self):
        print(self.inkcolor,self.company,self.size,self.shape )
               