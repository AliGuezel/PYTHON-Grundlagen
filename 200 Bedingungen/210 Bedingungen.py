# - Schlüsselwörter: if, elif, else
# - Vergleichsoperatoren: <, <=, >, >=, !=, ==
# - Abschluß der Bedingungsauswertung mit :
# - der Block, der bedingt ausgeführt werden soll, wird
#   durch Einrückung definiert
# - mehrere Bedingungen können durch and oder or verknüpft
#   werden

Zahl1 = 42
Zahl2 = 10

if Zahl1 > Zahl2:
    print("Zahl1 ist größer als Zahl2")

if Zahl2 < Zahl1:
    print("Zahl2 ist kleiner als Zahl1")

if Zahl1 != Zahl2:
    print("Zahl1 unterscheidet sich von Zahl2")

if Zahl1 % 2 == 0:
    print("Zahl1 ist eine gerade Zahl")

if Zahl1 >= Zahl2:
    print("Zahl1 ist größer als oder gleich Zahl2")
else:
    print("Zahl1 ist kleiner als Zahl2")
    
if Zahl1 > Zahl2:
    print("Zahl1 ist größer als Zahl2")
elif Zahl1 == Zahl2:
    print("Zahl1 und Zahl2 sind gleich")
else:
    print("Zahl1 ist kleiner als Zahl2")