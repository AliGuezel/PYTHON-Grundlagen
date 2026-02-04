# die unterste Funktion verarbeitet die Ausnahme

def Berechnen(Zahl):
    try:
        return 42 / Zahl
    except:
        print("Fehler in Berechnen")
       
def ZahlErmitteln():
    return Berechnen(int(input("Geben Sie eine Zahl ein: ")))

print(ZahlErmitteln())
