# die mittlere Funktion verarbeitet die Ausnahme

def Berechnen(Zahl):
    return 42 / Zahl
       
def ZahlErmitteln():
    try:
        return Berechnen(int(input("Geben Sie eine Zahl ein: ")))
    except:
        print("Fehler in ZahlErmitteln")

print(ZahlErmitteln())
