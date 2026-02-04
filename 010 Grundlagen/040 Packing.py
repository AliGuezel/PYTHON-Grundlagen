
# erzeugt einen tuple:
Datum = 4, 3, 2020
print(type(Datum), Datum)

# anschließend kann auf die einzelnen Elemente des Tupels zugegriffen werden
Tag = Datum[0]
Monat = Datum[1]
Jahr = Datum[2]
print("Tag:", Tag)
print("Monat:", Monat)
print("Jahr:", Jahr)

# die Zuweisung kann aber auch durch Unpacking vereinfacht werden:
# Python verteilt dabei die einzelnen Elemente auf die Variablen
Tag, Monat, Jahr = Datum

# die automatische Zuweisung funktioniert nur, wenn die Anzahl der
# Zielvariablen der Anzahl der Element entspricht
# nachfolgende Anweisung funktioniert nicht:
# Start, Mitte, Ende = (1, 2, 3, 4, 5, 6, 7, 8)

# ein Asterisks (*) kann dabei dann aber eingesetzt werden, um ver-
# bleibende (restliche) Elemente als liste einer Variablen zugewiesen
# wird:
Start, *Mitte, Ende = (1, 2, 3, 4, 5, 6, 7, 8)
print(Start, Mitte, Ende)

# dieses Unpacking kann auch verwendet werden, um aus einer Sammlung
# eine ausgepackte Menge einzelner Elemente erstellen zu lassen. Nach-
# folgend wird eine Zeichenfolge durch den Asteriks (*) ausgepackt
# und durch die eckigen Klammern in eine Liste ungewandelt
s = "Hallo Welt"
c = [*s]
print(c)

# Umgekehrt ist es auch möglich, einzelne Werte zu verpacken, was letzt-
# lich nur eine einfache (definierende) Zuweisung ist:
Kombi = (1, 2)
# mit nur einem Wert:
Kombi = (1, )
# oder durch Iterationen erstellt
Liste1 = ["A", "B", "C"]
Liste2 = ["X", "Y", "Z"]
for Buchstabe1 in Liste1:
    for Buchstabe2 in Liste2:
        Kombi = (Buchstabe1, Buchstabe2)
        print(Kombi)

# mit Unpacking lassen sich auch die Schlüssel-
# Wert-Paare eines Dictionaries differenzieren
d = { "A" : "ABC", "D" : "DEF", "G" : "GHI" }
for s, w in d.items():
    print(s, w)