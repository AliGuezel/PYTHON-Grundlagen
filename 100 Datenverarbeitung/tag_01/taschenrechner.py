zahl1 = int(input("1. Zahl: "))
zahl2 = int(input("2. Zahl: "))
Rechenzeichen = input("Addieren? (+), Subtrahieren? (-), Multiplizieren? (*), Dividieren? (/): ")

Ergebnis = 0
if Rechenzeichen == "+":
    Ergebnis = zahl1+zahl2
elif Rechenzeichen == "-":
    Ergebnis = zahl1-zahl2
elif Rechenzeichen == "*":
    Ergebnis = zahl1*zahl2
elif Rechenzeichen == "/":
    Ergebnis = zahl1/zahl2

print("Das Ergebnis ist:", Ergebnis)

