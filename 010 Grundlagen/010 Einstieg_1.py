# https://o7planning.org/de/11421/anleitung-python-exception


#syntaktischer Fehler
# es fehlt die Umwandlung des (Eingabe-)Strings in eine Zahl
# das Programm bricht in der entsprechenden Zeile ab
Zahl = input("Geben Sie eine Zahl ein: ")
print(42 / Zahl)

# Lösung (Korrektur)
Zahl = input("Geben Sie eine Zahl ein: ")
print(42 / int(Zahl))

# logischer Fehler
# Aufgabe: es sollen vier Runden gelaufen werden
# Es werden aber fünf!
GeforderteRunden = 4
GelaufeneRunden = 0
while GeforderteRunden >= GelaufeneRunden:
    print("Ich laufe, also bin ich - und zwar jetzt bei Runde", GelaufeneRunden + 1)
    GelaufeneRunden += 1

# Lösung (Korrektur)
GeforderteRunden = 4
GelaufeneRunden = 0
while GeforderteRunden > GelaufeneRunden:
    print("Ich laufe, also bin ich - und zwar jetzt bei Runde", GelaufeneRunden + 1)
    GelaufeneRunden += 1

# nachfolgender Code hat zwei potentielle Fehlerquellen:
# a) Anwender gibt 'Die Morde des Herrn ABC' ein
# b) Anwender gibt eine 0 ein (Korrekte Zahl, aber Division durch 0)
Zahl = input("Geben Sie eine Zahl ein: ")
print(42 / Zahl)

# defensive Programmierung: vor 'kritischen Stellen' werden
# sämtliche Daten geprüft
Zahl = input("Geben Sie eine Zahl ein: ")

if not Zahl.isdigit():
    print(Zahl, "ist keine Zahl")
elif int(Zahl) == 0:
    print("es kann nicht durch 0 geteilt werden")
else:
    print(42 / int(Zahl))

# noch problematischer ist die defensive Programmierung bei 
# Verwendung von Funktionen
def Berechnen(Zahl):
    return 42 / Zahl
print(Berechnen(int(input("Geben Sie eine Zahl ein: "))))

# Defensiv im Aufrufer:
Zahl = int(input("Geben Sie eine Zahl ein: "))
print(42 / Zahl if Zahl != 0 else 0)

# Defensiv in der Funktion
def BerechnenDefensiv(Zahl):
    return 42 / Zahl if Zahl != 0 else 0
print(BerechnenDefensiv(int(input("Geben Sie eine Zahl ein: "))))

# Ausnahmebehandlung, einfachste Form:
Zahl = input("Geben Sie eine Zahl ein: ")
try:
    print(42 / int(Zahl))
except:
    print("Fehler")
print("Abschluß")

# mehrzeilige Aweisungen
Zahl = input("Geben Sie eine Zahl ein:")
try:
    print("Sie haben", Zahl, "eingegeben")
    print(42 / int(Zahl))
except:
    print("Es ist ein Fehler aufgetreten")
    print("Konzentrieren Sie sich, Heilandzack")

# finally
def Berechnen(Zahl):
    try:
        print(42 / int(Zahl))
    except:
        print("Fehler")
    finally:
        print("im finally-Block")

print(Berechnen(0))

# finally wird auch dann ausgeführt, wenn im except-Block
# aus der Funktion herausgesprungen wird
def Berechnen(Zahl):
    try:
        print(42 / int(Zahl))
    except:
        print("Fehler")
        return None
    finally:
        print("im finally-Block")
    print("Ende")

print(Berechnen(0))

