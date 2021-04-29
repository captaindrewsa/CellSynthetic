import time

class Compound():

    def __init__(self, name, graph):
        self.NAME = name
        self.FORMULA = graph
    
    def GetFormula(self):
        return self.FORMULA
    def GetName(self):
        return self.NAME

class Protein():
    NAME = ""
    WORKFLOW = []
    PARENT_COMPARTMENT = ""
    
    def __init__(self, name, parcomp):
        self.NAME = name
        self.PARENT_COMPARTMENT = parcomp

    def GetInputSubstance(self):
        pass

    def Function(self, *args):
        pass

    def GiveOutputSubstance(self):
        pass





class Compartment():
    NAME = ""
    COMPONENTS = {"Proteins":[],"Compounds":[],"Compartments":[]}
    MEM_COMP = {"Proteins":[],"Compounds":[]}

    def SetComponents(self, **kwargs):
        for types,item in kwargs.items():
            if types=="Proteins":
                self.COMPONENTS["Proteins"].append(item)
            if types=="Compounds":
                self.COMPONENTS["Compounds"].append(item)
            if types=="Compartments":
                self.COMPONENTS["Compartments"].append(item)
    
    def SetMemComponents(self, **kwargs):
        for types,item in kwargs.items():
            if types=="Proteins":
                self.COMPONENTS["Proteins"].append(item)
            if types=="Compounds":
                self.COMPONENTS["Compounds"].append(item)
    
    def GetComponents(self):
        return [self.COMPONENTS, self.MEM_COMP]


Comp1 = Compartment()
ProteinsTest = Protein("TestPROT",Comp1)
CompTest = Compound("Comp",3)

Comp1.SetComponents(Proteins=[ProteinsTest],Compounds=[CompTest])


while True:
    


