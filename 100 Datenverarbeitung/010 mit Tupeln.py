
# Es gibt in der Informatik zwei grundlegende Datenstrukturen:
#                           https://de.wikipedia.org/wiki/Datenstruktur
# - Array                   https://de.wikipedia.org/wiki/Feld_(Datentyp)
# - Datensatz               https://de.wikipedia.org/wiki/Datensatz

# 1. Mit Tupel können mehrere gleichartige Elemente in einer Liste
#    gesammelt werden

Primzahlen = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97);

# diese Sammlung der Primzahl läßt sich nun verwenden:
# Ausgabe
for z in Primzahlen:
    print(z)

# es kann geprüft werden, ob die von einem Anwender eingegebene Zahl eine Primzahl ist:
z = int(input("Zahl: "))
print(z in Primzahlen)

# es kann die Quersumme gebildet werden
Summe = 0
for z in Primzahlen:
    Summe += z
print(Summe)

# Zeichenfolgen können gesammelt werden
Monate = (
            "Januar", 
            "Februar", 
            "März", 
            "April", 
            "Mai", 
            "Juni", 
            "Juli", 
            "August", 
            "September", 
            "Oktober", 
            "November", 
            "Dezember" 
          )

s = input("Geben Sie eine Zahl für einen Monat ein: ")
print(Monate[int(s) - 1])

# 2. dadurch, daß unterschiedliche Daten in einem Tupel kombiniert werden können,
#    eignen sich Tupel auch um Datenstrukturen zu realisieren, z.B. eine Adresse
Adresse = ( "Gottlieb Zürn", "Bodenseegasse 7", "Konstanz")

# Hier zeigt sich auch der Sinn von Unpacking:
(Name, Strasse, Ort) = Adresse
print(Name)
print(Strasse)
print(Ort)

# diese beiden Varianten können nun kombiniert werden, um z.B. eine Liste 
# mit Adressen zu erzeugen
Adressen = (
                ( "Gottlieb Zürn", "Bodenseegasse 7", "Konstanz"),
                ( "Anselm Kristlein", "Obergassen 11", "München"),
                ( "Josef Georg Gallistl", "Kurzweg 23", "Breisgau"),
           )
print(Adressen)

# damit lassen sich dann einige Umsetzungen realisieren, 
# z.B. eine Liste aller Orte
for a in Adressen:
    print(a[2])

# Beispiel für gesteigerte Lesbarkeit
for a in Adressen:
    (Name, Strasse, Ort) = a
    print("{strasse}: {name}".format(strasse=Strasse, name=Name))