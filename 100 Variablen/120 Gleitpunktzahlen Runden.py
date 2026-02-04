# für manche Programmierungen ist es notwendig Zahlen zu runden
# Hierfür steht eine eingebaute Methode zur Verfügung: round()
# 
# Als Parameter wird die Zahl übergeben, die gerundet werden soll.
# Es gibt eine Variante der Methode round, bei der angegeben werden
# kann, bis zu welcher Stelle gerundet werden soll

z = 13.8376
d = round(z)
print(d)

d = round(z, 2)
print(d)

# Beispiel für Verschachtelung
print(round(12.237, 2))

# Berechnung geht von innen nach außen
# erst wird gerundet
# dann wird das Ergebnis ausgegeben
x = round(12.237, 2)
print(x)