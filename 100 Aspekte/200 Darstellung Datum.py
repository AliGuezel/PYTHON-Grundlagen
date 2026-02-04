import time
import datetime
import locale

# die erste Herausforderung im Zusammenhang mit Datumswerten ist 
# ihre Darstellung.
# Datumsformate: https://de.wikipedia.org/wiki/Datumsformat
# Verbindlich für die Darstellung ist eigentlich die ISO 8601:
# https://de.wikipedia.org/wiki/ISO_8601
# Bei der Standardausgabe wird diese Norm berücksichtigt:
Datum = datetime.datetime.now()
print(Datum)

# die Darstellung im ISO-Format kann auch explizit angegeben werden,
# die Verwendung der Methode macht aber keinen Unterschied
print(Datum.isoformat())

# eine weitere Variante zur Darstellung eines Datums als String:
print(Datum.ctime())

# Um die Darstellung bis in alle Einzelheiten differenziert steuern
# zu können, steht die Methode strftime zur Verfügung
# Übersicht über die einzelnen Formatelemente: 
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
print(Datum.strftime("%d.%m.%Y"))

# Das Problem dabei ist, daß die Ausgabe in US-amerikanisch erfolgt
print(Datum.strftime("%B"))

# Soll die Ausgabe in einer anderen Sprache erfolgen, muß diese
# Sprache explizit eingestellt werden:
locale.setlocale(locale.LC_ALL, "de-DE")
print(Datum.strftime("%B"))
print(Datum.strftime("%A"))

# die Methode ctime bleibt davon allerdings unberührt
print(Datum.ctime())

# die Methode strftime kann auch für die Ausgabe der Zeit 
# verwendet werden
print(Datum.strftime("%H:%M"))

# es gibt auch Formatanweisungen, die automatisch die jeweils
# aktive Sprache (Kultur) verwendet
print(Datum.strftime("%c"))
print(Datum.strftime("%x"))
print(Datum.strftime("%X"))

locale.setlocale(locale.LC_ALL, "en-US")
print(Datum.strftime("%c"))
print(Datum.strftime("%x"))
print(Datum.strftime("%X"))
