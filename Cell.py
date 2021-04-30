import Compounds, Compartments, Proteins

class Cell():
    """
    Модуль Cell отвечает за манипуляциями связанными с самой клеткой и всем в ней находящимся

    __init__ - конструктор клетки, основанный на обязательном нахождении внутри какого-либо компартмента (по умолчанию - окружение). Сама по себе клетка не является компартментом

    AddCompartment - создает дочерний к самой клетке (если не указан параметр mother_compartment) или к другому компартменту компартмент.


    """
    
    
    NAME = ""               
    ENVIROMENT = 0          
    COMPARTMENTS = {}
    PROTEINS = {}
    COMPOUNDS = {}
    mPROTEINS = {}
    mCOMPOUNDS = {}

    def __init__(self, name, Enviroment):           
        self.NAME = name                            
        self.ENVIROMENT = Enviroment

    
    def SetCompartment(self, name):                                                                                    
        Com = Compartments.Compartment(name, self)                                   
        self.COMPARTMENTS[name]=Com                                                                                       

    def SetComponents(self):
        pass



    def __getitem__(self, name):               
        if name in list(self.COMPARTMENTS):    
            return self.COMPARTMENTS[name]     
        else:
            return "ERROE! Compartments not found!"    

    def __str__(self):
        return "Имя:{}\nОкружение:{}\nКомпартменты:{}".format(self.NAME,self.ENVIROMENT.NAME,list(self.COMPARTMENTS.keys())) 

    
