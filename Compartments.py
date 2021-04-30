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

    def SetComponents(self, proteins:dict=None, compounds:dict=None, compartments:dict=None, mproteins:dict=None, mcompounds:dict=None):
        pass

    
    def GetComponents(self):
        return [self.COMPONENTS, self.MEM_COMP]
    
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