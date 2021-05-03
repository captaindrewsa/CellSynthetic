class Compartment():
    NAME = ""
    PARENT_COMPARTMENT = None
    PROTEINS = {}
    COMPOUNDS = {}
    COMPARTMENTS = {}
    mPROTEINS = {}
    mCOMPOUNDS = {}

    def __init__(self, name, parent_compartment = None):
        self.NAME = name
        self.PARENT_COMPARTMENT = parent_compartment
    def __str__(self):
        return (f"Имя: {self.NAME}\nРодительский компартмент: {self.PARENT_COMPARTMENT.NAME if self.PARENT_COMPARTMENT != None else 'Отсутствует'}\nКомпартменты: {list(self.COMPARTMENTS.keys())}")
    
    def AppendCompartmentToDict(self, compartment):
        self.COMPARTMENTS[compartment.NAME]=compartment





    