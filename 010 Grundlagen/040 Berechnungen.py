import datetime

# mit datetime.timedelta können Zeitspannen verwaltet werden
# ein Delta kann z.B. durch Berechnung mit zwei Datumswerten 
# erzeugt werden
Datum1 = datetime.datetime(2000, 4, 5, 12, 0, 0)
Datum2 = datetime.datetime(2010, 8, 9, 14, 30, 0)
Delta = Datum2 - Datum1
print(Delta)
print(Delta.days, Delta.seconds, Delta.microseconds)

# das Delta kann auch negativ sein, aber ACHTUNG:
# nur der Tageswert ist negativ
Delta = Datum1 - Datum2
print(Delta)

# das Delta ist letztlich eine Zahl, folglich kann mit ihm
# gerechnet werden
Delta1 = datetime.date(2020, 3, 12) - datetime.date(2020, 3, 2)
Delta2 = datetime.date(2020, 4, 22) - datetime.date(2020, 4, 10)
print(Delta1 + Delta2)
  
# timedelta kann auch verwendet werden,
# um Berechnungen mit einem Datum durchzuführen
# (Additionen, Subtraktionen)
Datum = datetime.datetime.now()
Delta = datetime.timedelta(days=45)
DatumNeu = Datum + Delta
print(DatumNeu)




