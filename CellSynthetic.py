import Compartments,Proteins,Compounds, Cell

def CreateEnviroment(name):
    return Compartments.Compartment(name)


def CreateCell(name, enviromet):
    return Cell.Cell(name, enviromet)


def Start():
    pass

def Stop():
    pass


