import CellSynthetic as cs

Enviroment = cs.CreateEnviroment("Env")
Cell = cs.CreateCell("Клетка",Enviroment)
cs.AddCompartment("ЭПР",Cell)


print(Cell)

'''
Enviroment = cs.CreateEnviroment("Окружение")
Cell = cs.CreateCell("Тестовая клетка", Enviroment)

cs.AddCompartment("Эпр",Cell)
cs.AddCompartment("Внешняя мембрана митохондрии",Cell)
cs.AddCompartment("Внутренняя мембрана митохондрии",Cell)

Organoid = cs.CreateCompartment("Хлоропласт") etc
cs.AddCompartment(Organoid,Cell)

Cell["Матрикс митохондрии"].AddComponents(proteins=["Hcp70","CUDA2"],compounds=["dff-3-sdfs","af1DG"])


Enviroment.start()



'''