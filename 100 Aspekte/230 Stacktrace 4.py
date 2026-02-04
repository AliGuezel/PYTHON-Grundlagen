# die oberste Ebene verarbeitet die Ausnahme

def Berechnen(Zahl):
    return 42 / Zahl
       
def ZahlErmitteln():
    return Berechnen(int(input("Geben Sie eine Zahl ein: ")))

try:
    print(ZahlErmitteln())
except:
    print("Fehler im Programm")
