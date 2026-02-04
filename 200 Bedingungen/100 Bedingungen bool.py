# Die Varianten für den Datentyp bool können auf die Verwendung
# in bedingten Ausdrücken übertragen werden
# Theoretisch läßt sich ja jede Auswertung in den Bedingungen
# in bool-Variablen zwischenspeichern:

a = 42
b = 15

pruef = a > b
if pruef:
    print("a ist größer als b")

# kürzer:
if a > b:
    print("a ist größer als b")

# da alle Datentpen in Wahrheitswerte übersetzt werden können,
# können sie in bedingten Ausdrücken verwendet werden
# zu beachten ist im nachfolgenden Beispiel auch, daß
# nicht mit == True oder == False verglichen wird, sondern
# daß der Wahrheitswert direkt umgesetzt wird
zahl = 1
if zahl:
    print("Zahl ist wahr")

zahl = 0
if not zahl:
    print("Zahl ist unwahr")

# Bedingungsausdrücke lassen sich negieren:
# Achtung: gleichbedeutend mit 'if Zahl != 10:
Zahl = 10
if not Zahl == 20:
    print("Zahl ist nicht 20")

# mehrere Bedingungsausdrücke lassen sich mit and kombinieren
if a > b and a % 2 == 0:
    print("a ist größer als b und a ist eine gerade Zahl")

# mehrere Bedingungsausdrücke lassen sich mit or kombinieren
if b > a or b % 2 != 0:
    print("entweder b ist größer als a oder b ist eine ungerade Zahl")


# die Reihenfolge der Auswertung läßt sich durch Klammersetzung beeinflußen

A = 1
B = 2
C = 3

if A == 1 or (B == 2 and C == 6):
    print("Variante1 paßt")

if (A == 1 or B == 2) and C == 6:
    print("Variante2 paßt")

# Wenn mehr als zwei Bedingungen verbunden werden und
# Und- und Oder-Verknüpfungen kombiniert werden, ist
# es sinnvoll, die Ergebnisse in 'sprechenden Variablen'
# zwischenzuspeichern:
A_Ist_1 = A == 1
B_Ist_2 = B == 2
C_Ist_6 = C == 6

if A_Ist_1 or (B_Ist_2 and C_Ist_6):
    print("Variante1 paßt")

if (A_Ist_1 or B_Ist_2) and C_Ist_6:
    print("Variante2 paßt")

