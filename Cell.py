    def __getitem__(self, name):               
        if name in list(self.COMPARTMENTS):    
            return self.COMPARTMENTS[name]     
        else:
            return "ERROR! Compartments not found!"    

    def __str__(self):
        return "Имя:{}\nОкружение:{}\nКомпартменты:{}".format(self.NAME,self.ENVIROMENT.NAME,list(self.COMPARTMENTS.keys())) 

    
