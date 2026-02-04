# in Python werden auch die speziell eingerichteten
# Properties (Eigenschaften) vererbt

class Basis:

    def __init__(self):
        self.__wert = 0

    @property
    def Wert(self):
        return self.__wert

    @Wert.setter
    def Wert(self, wert):
        self.__wert = wert

class Ableitung(Basis):
    pass

a = Ableitung()
print(a.Wert)
a.Wert = 90
print(a.Wert)