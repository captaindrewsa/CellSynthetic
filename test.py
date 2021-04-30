import CellSynthetic as cs


Enviroment = cs.CreateEnviroment("TestEnv")

Cell = cs.CreateCell("TestCell",Enviroment)
Cell.AddCompartment("ЭПР")
Cell.AddCompartment("ШЭПР", "ЭПР")

print(Cell["ШЭПР"])
