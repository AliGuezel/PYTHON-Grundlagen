# wie die Darstellung kann natürlich auch die Eingabe eines 
# Datums in den unterschiedlichsten Formaten erfolgen
# auch hierfür stehen einige Möglichkeiten zur Verfügung
#
# zu beachten ist auch hier, daß die Umsetzungen auf
# der Basis der aktuellen Kultureinstellungen erfolgen

import datetime
import locale
from dateutil.parser import *

locale.setlocale(locale.LC_ALL, "de_DE")

DatumString = datetime.datetime.now().strftime("%x")
print(DatumString)
Datum = datetime.datetime.strptime(DatumString, "%x")
print(Datum)

Format = "%d.%m.%Y"
DatumString = datetime.datetime.now().strftime(Format)
Datum = datetime.datetime.strptime(DatumString, Format)
print(Datum)

Eingabe = input("Geben Sie ein Datum ein: ")
Datum = datetime.datetime.strptime(Eingabe, "%x")
print(Datum)

# neben der 'formatierten Übernahme' stehen auch
# standardisierte Varianten zur Verfügung:
DatumString = datetime.datetime.isoformat(datetime.datetime.now())
print(DatumString)
Datum = datetime.datetime.fromisoformat(DatumString)
print(Datum)

# die Möglichkeiten der Standard-Bibliothek sind
# etwas 'unflexibel', weshalb es einige weitere 
# Bibliotheken gibt, die 'abweichende' Eingaben
# interpretieren können
# weitere Hinweise: 
# https://dateutil.readthedocs.io/en/stable/examples.html#parse-examples
# (in dieser Bibliothek sind natürlich weitere nützliche Funktionen enthalten)
Eingabe = input("Geben Sie ein Datum ein: ")
Datum = parse(Eingabe)
print(Datum)