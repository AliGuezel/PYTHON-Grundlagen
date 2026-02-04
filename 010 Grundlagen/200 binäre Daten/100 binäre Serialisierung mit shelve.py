# Mit dem Modul/shelve können auf einfache Weise
# Daten gespeichert werden.
# Unter Windows werden drei Dateien erzeugt (bei
# Verwendung anderer Betriebssysteme weicht das
# davon ab, nur eine (?)).
# In die erzeugte Datei wird eine Key-Value-Liste
# im binären Format geschrieben, die Werte können
# dann über den Schlüssel auch wieder ausgelesen
# werden.
# shelve erzeugt also eine Art dictionary. Ent-
# sprechend ist es auch möglich, die Schlüssel und
# die Werte als solche als Listen auszulesen .

import shelve

DateiName = "D:/Tmp/Daten"
Datei = shelve.open(DateiName)
Zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Datei['Zahlen'] = Zahlen
Datei.close()

Datei = shelve.open(DateiName)
Zahlen = Datei['Zahlen']
print(Zahlen)

ListeMitSchluesseln = list(Datei.keys())
print(ListeMitSchluesseln)
ListeMitWerten = list(Datei.values())
print(ListeMitWerten)

DateiName = "D:/Tmp/Monate"
Datei = shelve.open(DateiName)
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
Datei['Monate'] = Monate
Datei.close()

Datei = shelve.open(DateiName)
Monate = Datei['Monate']
print(Monate)

