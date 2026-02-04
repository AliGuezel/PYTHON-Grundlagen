# Boolsche Datentypen ermöglichen beliebige Kombinationen
#
# einfache Verwendung; ein Wahrheitswert kann negiert werden
#
# Verwendung von zwei Wahrheitswerten, die kombiniert werden:
# and - beide Variablen müssen True sein, damit die Kombination True ist
# or  - nur eine der beiden Variablen muß True sein, damit die Kombination
#       True ist

# Negation
print(True)
print(not True)

# Kombination mit and
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Kombination mit or
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Beispiele mit konkreten Zahlen
x = 1
y = 2
print(x == 1 and y == 2)
print(x == 1 and y == 6)

print()
print(x == 1 or y == 2)
print(x == 1 or y == 6)

# natürlich können auch mehr als nur zwei Ausdrücke miteinander
# kombiniert werden
# die Auswertungreihenfolge kann auch hier durch Klammersetzung 
# beeinflußt werden:
print((True or False) and False)
print(True or (False and False))

# Zahlenbeispiel
x = 1
y = 2
z = 3
print(x == 1 or (y == 2 and z == 6))
print((x == 1 or y == 2) and z == 6)

# or ist eigentlich überflüssig...
a = True
b = False
print(a or b)
print(not(not(a) and not(b)))

