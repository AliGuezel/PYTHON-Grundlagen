# die mittlere Funktion verarbeitet die Ausnahme
# die Ausnahmebehandlung im Programm wird deshalb
# nie verwendet

def Berechnen(Zahl):
    return 42 / Zahl
       
def ZahlErmitteln():
    try:
        return Berechnen(int(input("Geben Sie eine Zahl ein: ")))
    except:
        print("Fehler in ZahlErmitteln")

try:
    print(ZahlErmitteln())
except:
    print("Fehler im Programm")

