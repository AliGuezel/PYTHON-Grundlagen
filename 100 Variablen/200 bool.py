# bool ist ein Datentyp mit zwei möglichen Werten: True und False
# explizite Zuweisung
wahr = True
print(wahr)
unwahr = False
print(unwahr)

# die beiden Werte können auch über eine 'Auswertung' zugewiesen werden
Zahl1 = 42
Zahl2 = 10

if Zahl1 > Zahl2:
    Zahl1IstGroesserAlsZahl2 = True
else:
    Zahl1IstGroesserAlsZahl2 = False
print(Zahl1IstGroesserAlsZahl2)

# implizite Zuweisung: Python erkennt, daß nach dem Gleichheitszeichen
# ein Bedingungsausdruck verwendet wird, stuft die Variable deshalb
# als einen bool ein
Zahl1IstGroesserAlsZahl2 = Zahl1 > Zahl2
print(Zahl1IstGroesserAlsZahl2)

# 'technisch korrekt', aber nicht in Gebrauch:
if Zahl1IstGroesserAlsZahl2 == True:
    print(Zahl1IstGroesserAlsZahl2)

# statt dessen:
if Zahl1IstGroesserAlsZahl2:
    print(Zahl1IstGroesserAlsZahl2)

# bool-Variablen haben einen Zahlenwert
print(int(False))
print(int(True))

# die Wahrheitswerte anderer Datentypen
print(bool(0))
print(bool(156))
print(bool(0.0))
print(bool(11.08))
print(bool(""))
print(bool("Text"))
