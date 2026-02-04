# auch wenn Python keine statisch typisierte Sprache ist, ist
# es möglich und in manchen Fällen sogar erforderlich, eine
# Variable in einen anderen Typ umzuwandeln
# in Python hat beispielsweise jeder Datentyp einen Wahrheitswert:
print(bool(0), bool(1))

# umgekehrt haben die Wahrheitswerte auch einen numerischen Wert
print(int(True), int(False))

# sehr häufig müssen Zeichenketten in Zahlen umgewandelt werden
# input z.B. erzeugt einen String, mit dem man aber nur rechnen
# kann, wenn man ihn vorher in eine Zahl umgewandelt hat:
s = input("Zahl: ")
Zahl = int(s)

# zu beachten ist, daß fehlerhafte Umwandlungen zu einem Fehler
# führen:
print(int("Eins"))

