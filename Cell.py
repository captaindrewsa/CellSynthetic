import Compounds, Compartments, Proteins

class Cell():
    NAME = ""               
    ENVIROMENT = 0          
    COMPARTMENTS = {}
    PROTEINS = {}
    COMPOUNDS = {}
    mPROTEINS = {}
    mCOMPOUNDS = {}

    def __init__(self, name, Enviroment):           #Инициализация
        self.NAME = name                            #объекта клетки
        self.ENVIROMENT = Enviroment

    
    def AddCompartment(self, name, mother_compartment= None):                               #Создается компартмент, по умолчанию дочерний к объекту Клетка
        if mother_compartment == None:                                                      #В случае указания дочернего элемента запускается проверка на 
            Com = Compartments.Compartment(name, self)                                      #наличие такового и создания компартмента дочерненго к данному элементу.
            self.COMPARTMENTS[name]=Com                                                     #В случае отсуствия такого - ошибка                                     
        elif mother_compartment in list(self.COMPARTMENTS):   
            Com = Compartments.Compartment(name, self.COMPARTMENTS[mother_compartment])
            self.COMPARTMENTS[name]=Com
        else:
            print("ERROR! There is no compartment with this name.")

    def SetComponents(self):
        pass



    def __getitem__(self, name):                #Позволяет получить досутп к компартменту по []
        if name in list(self.COMPARTMENTS):     #
            return self.COMPARTMENTS[name]      #
        else:
            return "ERROE! Compartments not found!"    

    def __str__(self):
        return "Имя:{}\nОкружение:{}\nКомпартменты:{}".format(self.NAME,self.ENVIROMENT.NAME,list(self.COMPARTMENTS.keys())) #Выводит общие данные о Клетке

    
