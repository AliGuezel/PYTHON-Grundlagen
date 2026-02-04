# bei den Übergabeparametern ist es möglich
# - positionale
# - benannte 
# - optionale 
# - beliebig viele
# Parameter zu verwenden

def PositionaleParameter(Zahl1, Zahl2):
    print(Zahl1, Zahl2)

PositionaleParameter(8, 9)


# ***** Parameter explizit benennen *****

def WertAusgeben(Wert):
    print(Wert)

WertAusgeben(42)
WertAusgeben(Wert = 42)

# Parameter benennen erhöht die Lesbarkeit des Codes
def DatumswerteAendern(Jahr, Monat, Tag):
    print("in Funktion", Jahr, Monat, Tag)
DatumswerteAendern(2020, 6, 5)
DatumswerteAendern(Jahr=2020, Monat=6, Tag=5)

# zumal die Reihenfolge keine Rolle spielt
# hilft Fehler zu vermeiden
DatumswerteAendern(Jahr=2020, Tag=5, Monat=6)

# Groß- und Kleinschreibung müssen beachtet werden
# WertAusgeben(wert = 42)


# ***** optionale Parameter *****

# werden Parameter mit Werten vorbelegt, 
# müssen sie nicht zugewiesen werden
# durch benannte Parameter wird das Problem gelöst,
# Parameter zu 'überspringen'
def OptionaleParameter(Zahl1 = 1, Zahl2 = 42):
    print(Zahl1 * Zahl2)

OptionaleParameter()
OptionaleParameter(2, 4)
OptionaleParameter(Zahl2 = 10)
OptionaleParameter(Zahl2 = 4, Zahl1 = 8)


# ***** beliebig viele Parameter *****
def ZahlenAusgeben(*Zahlen):
    print("hier kommen Zahlen:")
    print(Zahlen)

ZahlenAusgeben(1, 2, 3)
ZahlenAusgeben(1)
ZahlenAusgeben()

# ***** Kombinationen *****

# auf beliebig viele Parameter folgen weitere Parameter
# die folgenden Parameter können nur benannt verwendet werden
def Variante1(*Werte, a, b):
    print(a, b)
# nachfolgender Aufruf kann nicht funktionieren, weil
# a und b keine Werte zugewiesen werden:
# Variante1(1, 2, 3)
# funktioniert, denn a und b werden angegeben
Variante1(8, 9, 11, a=7, b=3)

# auf 'normale' Parameter folgen beliebig viele Parameter
# funktioniert, weil die ersten beiden Werte
# positional zugewiesen werden können
def Variante2(a, b, *Werte):
    print(a, b)
Variante2(2, 5, 1, 2, 9)

# beliebig viele Parameter stehen in der Mitte
# mehrere Parameter können auch mittendrin angegeben werden,
# dann müssen natürlich die folgenden Parameter benannt 
# verwendet werden
def Variante3(a, b, *Werte, c, d):
    print(a, b, c, d)
Variante3(8, 9, 10, 11, 12, c=13, d=14)

# Der Zwang zur Abdeckung entfällt dann natürlich bei
# optionalen Parametern
def Variante4(a, b, *Werte, c = 76, d = 89):
    print(a, b, c, d)
Variante4(8, 9, 10, 11, 12, d=14)


