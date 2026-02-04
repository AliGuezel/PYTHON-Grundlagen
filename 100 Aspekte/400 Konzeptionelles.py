

class Auto:
    def __init__(self, ps):
        self.__PS = ps
    @property
    def PS(self):
        return self.__PS
    @PS.setter
    def PS(self, ps):
        if ps > 200:
            raise ValueError("zu viele PS")
        self.__PS = ps

def GetAutoliste():
    return [
                Auto(90),
                Auto(120),
                Auto(110),
                Auto(75)
           ]

def Ausgabe(Autos):
    for a in Autos:
        print(a.PS)

def TuningOhneAusnahmeBehandlung(Autos):
    for a in Autos:
        a.PS *= 2

def TuningMitAusnahmeBehandlung1(Autos):
    try:
        for a in Autos:
            a.PS *= 2
    except ValueError as e:
        print(e)

def TuningMitAusnahmeBehandlung2(Autos):
    for a in Autos:
        try:
            a.PS *= 2
        except ValueError as e:
            print(e)


# Liste = GetAutoliste()
# TuningOhneAusnahmeBehandlung(Liste)

# Liste = GetAutoliste()
# TuningMitAusnahmeBehandlung1(Liste)
# Ausgabe(Liste)

Liste = GetAutoliste()
TuningMitAusnahmeBehandlung2(Liste)
Ausgabe(Liste)

