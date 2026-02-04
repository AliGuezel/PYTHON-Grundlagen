# eine in einer Funktion definierte Variable ist
# nur in der Funktion gültig,
# Code, der sich außerhalb der Funktion befinndet,
# kann diese Variable (erst einmal) nicht verwenden
def Funktion():
    Wert = 9
    print(id(Wert), Wert)

Funktion()
print(Wert)


# funktioniert, die untergeordnete Methode
# kann auf die Variable des Hauptprogramms zugreifen
def ZugriffInMethodeAufGlobaleVariable():
    print(Zahl, "(in Methode)")

Zahl = 666
ZugriffInMethodeAufGlobaleVariable()


# funktioniert nicht
# die untergeordnete Methode kann die globale
# Variable nicht 'einfach' ändern
# def ZugriffInMethodeAufGlobaleVariable():
#     Zahl = Zahl * 2
#     print(Zahl, "(in Methode)")
#
# Zahl = 666
# ZugriffInMethodeAufGlobaleVariable()


# funktioniert, weil Zahl jetzt als lokale Variable ->neu<- definiert wurde
# dann kann mit ihr wie mit einer normalen lokalen Variablen gearbeitet
# werden
def ZugriffInMethodeAufGlobaleVariable():
    Zahl = 42.
    print(id(Zahl), Zahl)

Zahl = 666
print(id(Zahl), Zahl)
ZugriffInMethodeAufGlobaleVariable()
print(id(Zahl), Zahl)



# funktioniert
# mit dem Schlüsselwort global wird die übergeordnete Variable
# gewissermaßen globalisiert, d.h. das nun auch ein ändernder
# Zugriff möglich ist und daß diese Änderung dauerhaft bleibt
def ZugriffInMethodeAufGlobaleVariable():
    global Zahl
    Zahl = Zahl * 2
    print(id(Zahl), Zahl, "(in Methode)")

Zahl = 666
print(id(Zahl))
ZugriffInMethodeAufGlobaleVariable()
print(id(Zahl), Zahl)
