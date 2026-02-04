# https://docs.python.org/3/library/csv.html

import csv

# Methodensignatur:
# csv.reader(csvfile, [dialect], {**fmtparam})
# - csvfile     Datei mit den Daten, muß ein mit open 
#               geöffnetes Dateiobjekt sein
# - dialect     es gibt keine verbindlich Formatierungen für csv
#               (Banken z.B. verwenden ; statt ,)
#               man kann in Python Formatangaben verwenden oder
#               Zusammenstellungen von typischen Formatierungen
#               in sogenannten Dialekten verwenden 
#               die zur Verfügung stehenden Dialekte kann
#               man mit csv.list_dialects() abrufen
# - fmtparam    Schlüsselwortparameter, mit denen die Formatierung
#               der Daten justiert werden können, ohne auf einen
#               Dialekt zurückgreifen zu müssen

# nach dem Einlesen steht ein iterierbares Objekt zur Verfügung

#reader = csv.reader(open("Daten2.csv"), delimiter=';')
#for row in reader:
#   print(row)

# reader = csv.reader(open(r"D:\Tmp\autos.csv"), delimiter=";")
# for row in reader:
#    print(row)


reader = csv.DictReader(open("Daten.csv"))
for row in reader:
    print(row)