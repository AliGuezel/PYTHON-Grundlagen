
# einfachste Funktion überhaupt, keine Übergabe, keine Rückgabe
def HalloWeltAusgeben():
    print("Hallo Welt")

HalloWeltAusgeben()


# Funktion mit einer einfachen Rückgabe
def HalloWeltErzeugen():
    return "Hallo Welt"

erg = HalloWeltErzeugen()
print(erg)
# oder
print(HalloWeltErzeugen())


# Funktion mit einer einfachen Übergabe
def ZahlAnzeigen(Zahl):
    print(Zahl)

ZahlAnzeigen(42)


# Funktion mit Übergabe-Parametern und Rückgabe
def Addition(Zahl1, Zahl2):
    return Zahl1 + Zahl2

print(Addition(20, 22))


# die Funktion muß immer vor ihrer ersten Verwendung
# definiert werden, ansonsten ist aber Ort und Reihen-
# folge egal
#FalscheReihenfolge()
#def FalscheReihenfolge():
#    print("!")

# Mehrfachverwendung von Funktionsbezeichnungen
# es wird die zuletzt definierte Funktion verwendet
def DoppelteFunktion():
    print("in doppelter Funktion 1")
#DoppelteFunktion()

def DoppelteFunktion():
    print("in doppelter Funktion 2")

DoppelteFunktion()