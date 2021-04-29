class Protein():
    NAME = ""
    PARENT_COMPARTMENT = 0
    def __init__(self, name, Compartment):
        self.PARENT_COMPARTMENT = Compartment
        self.NAME = name
    def GetInputSubstance(self, proteins, compounds):
        pass
    def Function(self, *args):
        pass
    def GiveOutputSubstance(self):
        pass