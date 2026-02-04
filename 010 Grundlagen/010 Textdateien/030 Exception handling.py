# Beim Arbeiten mit Dateien sollte immer ein Exception-Handling 
# eingebaut werden, weil es eine ganze Reihe von Ausnahmen geben kann:
# - Datei wurde gelöscht
# - Benutzer hat keine Berechtigung
# - Server steht nicht zur Verfügung

# erzeugt einen Fehler, weil die Datei nicht existiert
# Datei = open("Gugelhupf.txt", "r")
# for Zeile in Datei:
#     print(Zeile)

try:
    Datei = open("Gugelhupf", "r")
except Exception as ex:
    print(type(ex))

# zu beachten ist aber dabei, daß das Betriebssystem die
# Datei sperrt, dem Betriebsystem muß also mitgeteilt 
# werden, daß die Datei nicht mehr gebraucht werden
# Das hat auch Auswirkungen auf das Exception-Handling
# Der Zugriff auf die Dateien muß ja in beiden Fällen
# aufgehoben werden: im Falle einer Ausnahme und im Falle,
# daß der Zugriff funktioniert

Datei = None 
try:
    Datei = open("Gugelhupf", "r")
    print(Datei.readlines())
except Exception as ex:
    print(type(ex))
finally:
    if Datei is not None:
        Datei.close()

try:
    with open("Gugelhupf", "r") as Datei:
        print(Datei.readlines())
except Exception as ex:
    print(ex)

