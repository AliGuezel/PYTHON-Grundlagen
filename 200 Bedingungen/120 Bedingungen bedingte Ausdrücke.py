# bedingte Ausdrücke sind eine Abkürzung, um Zuweisungen
# als Einzeiler ein wenig knapper formulieren zu können
# etwas Yoda-mäßig:
# x soll sein 20 wenn zahl == 10 sonst eben 30

zahl = 15
x = 20 if zahl == 10 else 30
print(x)

# bedingte Ausdrücke können auch für etwas komplexere
# Verschachtelungen mißbraucht werden
a = 21
b = 3
x = (a * 2 if(a > 10 and b < 5) else b * 2)
print(x)

