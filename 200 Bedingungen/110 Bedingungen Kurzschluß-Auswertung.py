# https://de.wikipedia.org/wiki/Kurzschlussauswertung
# kurzschlüssige Auswertung (short-circuit evaluation):
# zunächst wird die erste Bedingung geprüft
# je nach Verknüpfung der Bedingung wird u.U. die zweite
# Bedingung gar nicht mehr ausgewertet

# Beispiel 1:
# die erste Bedingung ist false
# beide Bedingungen sind mit and verknüpft
# es müssen also beide Bedingungen zutreffen
# da die erste bereits falsch ist, macht es keinen Sinn,
# die zweite Bedingung noch zu prüfen
x = False
if x and print("Lazy"):
    print("Test")

# das kann man sich zunutze machen, um einen Fehler
# durch eine Division durch 0 zu vermeiden.
# Normalerweise führt nachfolgender Code zu einem
# Laufzeitfehler
#zahl = 0
#if 42 / zahl > 10:
#    print("funktioniert nicht")

# nachfolgende Variante funktioniert, weil zunächst
# geprüft wird, ob die Zahl nicht 0 ist. Da die Zahl
# 0 ist, wird der zweite Teil, also die Division 
# durch 0 nicht mehr durchgeführt
zahl = 0
if zahl != 0 and 100 / Zahl > 10:
    print("funktioniert bei and")

# die kurzschlüssige Auswertung funktioniert auch
# bei einer Verknüpfung mit or:
if zahl == 0 or 42 / zahl > 1:
    print("funktioniert bei or")

