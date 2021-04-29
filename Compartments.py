class Compartment():
    NAME = ""
    COMPONENTS = {"Proteins":[],"Compounds":[],"Compartments":[]}
    MEM_COMP = {"Proteins":[],"Compounds":[]}

    def __init__(self, name, Compartment = None):
        self.NAME = name
        self.PARENT_COMPARTMENT = Compartment

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