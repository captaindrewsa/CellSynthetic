class Compartment():
    NAME = ""
    PARENT_COMPARTMENT=0
    PROTEINS = {}
    COMPOUNDS = {}
    COMPARTMENTS = {}
    mPROTEINS = {}
    mCOMPOUNDS = {}

    def __init__(self, name, Compartment = None):
        self.NAME = name
        self.PARENT_COMPARTMENT = Compartment

    def SetProteins(self, proteins:dict):
        pass
    def SetMProteins(self, mproteins:dict):
        pass
    def SetCompounds(self, compounds:dict):
        pass
    def SetMCompounds(self, mcompounds:dict):
        pass
    def SetComparment(self, compartment:dict):
        pass

    
    def GetComponents(self):
        pass
    
    def __call__(self):
        return "Вызов Call"
    
    def __str__(self):
        return "Имя: {}\nРодительский компартмент: {}\nБелки: {}\nВещества: {}\nКомпартменты: {}\nМемебранные Белки: {}\nМембранные вещества: {}".format(self.NAME,
        self.PARENT_COMPARTMENT.NAME,
        self.PROTEINS,
        self.COMPOUNDS,
        self.COMPARTMENTS,
        self.mPROTEINS,
        self.mCOMPOUNDS)