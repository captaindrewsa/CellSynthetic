import Compartments, Compounds, Proteins

def CreateEnviroment(name):
    return Compartments.Compartment(name)


def CreateCell(name, enviroment):
    Com = Compartments.Compartment(name, enviroment)
    _AppendCompartmentToEnvDict(Com, enviroment)
    return Com
    

    

def AddCompartment(compartment_name, par_compartment):
    if isinstance(par_compartment, Compartments.Compartment):
        Com = Compartments.Compartment(compartment_name, par_compartment)
        par_compartment.AppendCompartmentToDict(Com)
        _AppendCompartmentToEnvDict(Com, par_compartment)
    elif isinstance(par_compartment,str):
        pass

def _AppendCompartmentToEnvDict(target_comparment:Compartments.Compartment ,parent_compartment:Compartments.Compartment):
    if parent_compartment.PARENT_COMPARTMENT==None:
        parent_compartment.AppendCompartmentToDict(target_comparment)
    else:
        _AppendCompartmentToEnvDict(parent_compartment.PARENT_COMPARTMENT)



def Start():
    pass

def Stop():
    pass


