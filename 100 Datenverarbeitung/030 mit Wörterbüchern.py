# 'intuitiverer' Zugriff auf die Auflistung der Monate

# Beispielzugriff zeigt, daß nicht umgerechnet werden muß,
# daß nicht daran gedacht werden muß, daß sich die Monatsziffer
# um -1 verschiebt
Monate = { 
             1 : "Januar", 
             2 : "Februar", 
             3 : "März", 
             4 : "April", 
             5 : "Mai", 
             6 : "Juni", 
             7 : "Juli", 
             8 : "August", 
             9 : "September", 
            10 : "Oktober", 
            11 : "November", 
            12 : "Dezember" 
         }
Monat = int(input("Geben Sie eine Zahl für den Monat ein: "))
print(Monate[Monat] if Monat in Monate else "nichts gefunden")

# Auto-Daten bisher
PKW = [ "UN PP 900", 90, ]
# Zugriff dann mit 'magischer Zahl', Risiko, daß die
# Reihenfolge verändert wird
print(PKW[0])

# Datenstrukturen können mit benannten Eigenschaften ausgestattet werden:
Fahrzeug = {}
Fahrzeug["Kennzeichen"] = "UN PP 900"
Fahrzeug["PS"] = 90
Fahrzeug["Hubraum"] = 2000
print(Fahrzeug)

# Zugriff dementsprechend:
print(Fahrzeug["Kennzeichen"])

# Initialisierung ist auch über leere Klammern möglich
Auto = { }
Auto["Kennzeichen"] = "DO KK 984"
Auto["PS"] = 100
Auto["Hubraum"] = 2000
print(Auto)

# Motor wird seperat 'gebaut'
Auto = { }
Auto["Kennzeichen"] = "DO KK 984"
Motor = { }
Motor["PS"] = 100
Motor["Hubraum"] = 2000
Auto["Motor"] = Motor
print(Auto)

# Motor wird sozusagen bereits im Auto gebaut
Auto = { }
Auto["Kennzeichen"] = "DO KK 984"
Auto["Motor"] = { }
Auto["Motor"]["PS"] = 100
Auto["Motor"]["Hubraum"] = 2000
print(Auto)


