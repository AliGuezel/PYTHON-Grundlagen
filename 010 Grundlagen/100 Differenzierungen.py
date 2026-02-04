
# Der Fehler/die Ausnahme kann spezialisiert werden
# dadurch können z.B. Fehlermeldungen zielgerichtet formuliert werden
Zahl = input("Geben Sie eine Zahl ein: ")
try:
    print(42 / int(Zahl))
except ZeroDivisionError:
    print("Es kann nicht durch 0 geteilt werden")

# Problem bei der oberen Version ist, daß die Eingabe einer
# Zeichenfolge, die nicht in eine Zahl umgewandelt werden kann,
# weiterhin zu einem Fehler führt, denn mit dieser Version
# ist festgelegt, daß nur ZeroDivisionError berücksichtig werden sollen

# Es gibt zwei verschiedene Lösungsansätze:
# Es werden mehrere verschiedene Ausnahmen in einem Tupel gesammelt:
Zahl = input("Geben Sie eine Zahl ein: ")
try:
    print(42 / int(Zahl))
except (ZeroDivisionError, ValueError):
    print("Fehler")

try:
    Zahl = int(input("Geben Sie eine Zahl ein: "))
except ValueError as ex:
    print(ex.args[0])

# oder aber die Ausnahmebehandlung wird mit unterschiedlichen
# Zweigen differenziert:
Zahl = input("Geben Sie eine Zahl ein: ")
try:
    print(42 / int(Zahl))
except ZeroDivisionError:
    print("Es kann nicht durch 0 geteilt werden")
except ValueError:
    print("Die Eingabe konnte nicht in eine Zahl umgewandelt werden")

# falsche Reihenfolge
# da alle Ausnahmen irgendwie eine 'Exception' sind,
# verzweigt alle Ausnahmebehandlung in den ersten Zweig
# nachfolgende Zweige werden niemals erreicht!
Zahl = input("Geben Sie eine Zahl ein: ")
try:
    print(42 / int(Zahl))
except Exception:
    print("Fehler")
except ValueError:
    print("Die Eingabe konnte nicht in eine Zahl umgewandelt werden")
except ZeroDivisionError:
    print("Es kann nicht durch 0 geteilt werden")

# richtige Reihenfolge:
# 0 und Die Morde des Herrn ABC werden speziell ausgewertet und zwar:
# bevor die allerallgemeinste Ausnahme ausgewertet wird.
Zahl = input("Geben Sie eine Zahl ein: ")
try:
    print(42 / int(Zahl))
except ZeroDivisionError:
    print("Es kann nicht durch 0 geteilt werden")
except ValueError:
    print("Die Eingabe konnte nicht in eine Zahl umgewandelt werden")
except Exception:
    print("Fehler")

