# datetime-Objekte sind zunächst unveränderlich
# es ist also nicht möglich, einen einzelnen Bestandteil
# (Monat) direkt zu verändern
# 
# Eine Möglichkeit, 'trotzdem' Werte zu verändern, besteht
# in der Verwendung der Methode replace
import datetime

Datum = datetime.datetime.now()
print("vorher:", Datum)

Datum = Datum.replace(year = 2010)
print("nachher:", Datum)



