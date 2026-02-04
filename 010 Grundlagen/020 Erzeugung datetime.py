
# datetime ist ein OOP-basiertes Modul, das insgesamt 
# intuitiver zu handhaben ist
import datetime

# datetime differenziert zwischen
# - date        (Datum)
# - time        (Zeit)
# - datetime    (Kombination von Datum und Zeit)

Datum = datetime.date(2020, 5, 31)
print(Datum)

Zeit = datetime.time(12, 34, 23)
print(Zeit)

DatumZeit = datetime.datetime(2020, 5, 31, 12, 34, 21)
print(DatumZeit)

# die Datums- und Zeitanteile können aus dem datetime
# extrahiert werden
Datum = DatumZeit.date()
print(Datum)

Zeit = DatumZeit.time()
print(Zeit)

# Zuweisung von aktuellen Werten
# der Unterschied: now kann eine Zeitzone
# übergeben werden
DatumZeit = datetime.datetime.now()
print(DatumZeit)

Datum = datetime.datetime.today()
print(Datum)

# sollte man mit time-Daten (weiter-) arbeiten wollen,
# stehen Umwandlungsmethoden zur Verfügung
print(Datum.timetuple())
print(DatumZeit.timetuple())