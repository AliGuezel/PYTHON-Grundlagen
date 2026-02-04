
# Wichtig ist also:
# die String-Methoden geben wieder einen String zurück

# damit ergeben sich zwei Mechanismen für strings

# 1.Verschachtelung
Zeichenfolge = "zeichenfolge"
print(Zeichenfolge.upper())

# 2. Kaskadieren, auch: fluid ...
print(Zeichenfolge.upper().rjust(50))
