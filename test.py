import CellSynthetic as cs


Enviroment = cs.CreateEnviroment("TestEnv")

Cell = cs.CreateCell("TestCell",Enviroment)
Cell.SetCompartment("ЭПР")

print(Cell["ЭПР"])