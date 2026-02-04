# Version 1: ohne Fehlerbehandlung, Programm stürzt ab

def Berechnen(Zahl):
    return 42 / Zahl
       
def ZahlErmitteln():
    return Berechnen(int(input("Geben Sie eine Zahl ein: ")))

print(ZahlErmitteln())



