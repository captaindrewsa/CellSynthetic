import Compounds, Compartments, Proteins

class Cell():
    NAME = ""
    ENVIROMENT = 0
    COMPARTMENTS = []
    COMPARTMENTS_NAME= []

    def __init__(self, name, Enviroment):
        self.NAME = name
        self.ENVIROMENT = Enviroment

    
    def AddCompartment(self, name, mother_compartment= None):
        if mother_compartment == None:
            Com = Compartments.Compartment(name, self)
            self.COMPARTMENTS.append(Com)
            self.COMPARTMENTS_NAME.append(name)
        if mother_compartment!= None and mother_compartment in self.COMPARTMENTS_NAME:
            for compart in self.COMPARTMENTS:
                if compart.NAME == mother_compartment:
                    Com = Compartments.Compartment(name, compart)
                    self.COMPARTMENTS.append(Com)
                    break
                else:
                    print("ERROR! There is no compartment with this name.")

    def __getitem__(self, name):
        #Добавить вызов компартмента как элемента списка и его модификацию таким образом

    
