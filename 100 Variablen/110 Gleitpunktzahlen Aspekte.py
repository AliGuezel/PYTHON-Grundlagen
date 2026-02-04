# Gleitpunktzahlen werden nicht mit einer festgesetzten Anzahl von Nachpunkt-
# stellen gespeichert. Gleitpunktzahlen sind somit immer ungenau
# (Un-) Genauigkeit
x = 1.0 - 0.9
print(x)

# Diese Ungenauigkeit führt zu zwei praktischen Problemen

# 1. Berechnungsergebnisse können falsch werden
# 2. Gleitpunktzahlen können niemals für Vergleiche herangezogen
#    werden:
print(1.0 - 0.9 == 0.1)

# Deshalb dürfen Gleitpunktzahlen auch niemals bei Schleifen
# verwendet werden
# zu beachten hier auch:
# += Operator
# endlos-Schleife

i = 0
while i != 1:
    print(i)
    i += 0.1

# Lösungsansatz
Zahl1 = 1
Zahl2 = 0.9
erg = (Zahl1 * 100 - Zahl2 * 100) / 100