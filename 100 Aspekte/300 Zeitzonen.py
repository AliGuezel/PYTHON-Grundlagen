# Genese der Zeitmessungen:
# - Ortszeit
#   https://de.wikipedia.org/wiki/Ortszeit
# - Berliner Zeit (1833, Bedarf entstand durch die Eisenbahn)
# - Einführung einer einheitlichen Zeit in Deutschland (1. April 1893)
#   https://de.wikipedia.org/wiki/Gesetz_betreffend_die_Einf%C3%BChrung_einer_einheitlichen_Zeitbestimmung
#   MEZ
# - UTC (koordinierte Weltzeit)
#   https://de.wikipedia.org/wiki/Koordinierte_Weltzeit
#   Grafik: https://upload.wikimedia.org/wikipedia/commons/0/07/Standard_Time_Zones_of_the_World_%28October_2015%29.svg
#
# Warum es Zeitzonen gibt:
# https://www.timeanddate.de/zeitzonen/welt
# Übersicht(en)
# https://www.zeitzonen.de/
# https://www.zeitzonenrechner.net/
#
# Liste mit den Zeitzonen und ihren Bezeichnungen
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
#
# alle bisherigen berechneten Zuweisungen für Datum-Zeit-Werte basierten auf der
# lokalen Zeit, für Deutschland also eine Zeit, die eine Stunde über der Greenwich-
# Zeit liegt
# Es gibt aber auch die Möglichkeit, die aktuellen Zeit auf der Basis von UTC
# ermitteln und zuweisen zu lassen
import datetime
# wird für Zeitzonen benötigt: muß installiert werden
import pytz
from dateutil.tz import *

# der Unterschied beträgt in der Sommerzeit +2 Stunden
# und in der Winterzeit 1 Stunde
print(datetime.datetime.utcnow())
print(datetime.datetime.now())

# bei den bisherigen Datums-Zuweisungen wurde keine Zeitzone
# festgelegt, solche DateTime-Objekte werden 'naiv' genannt
Datum = datetime.datetime.now()
print(Datum)

# es ist aber auch möglich, bei Einrichtung des Datums eine
# Zeitzone zu hinterlegen, die Variante erzeugt dann ein 
# 'bewußtes' Datum
#
# in der ersten Variante wird das Zeitzonen-Objekt
# 'manuell' erstellt
#
# der wichtige Unterschied zu den vorangegangenen Fassungen
# besteht darin, daß der Datumswert 'seine Verschiebung' mit
# verwaltet - was die ISO-Ausgabe zeigt
Zeitzone = datetime.timezone(datetime.timedelta(hours=+9), name="Irgendwo")
Datum = datetime.datetime.now(Zeitzone)
print(Datum, Datum.strftime("%Z"))
print(Datum.isoformat())

# mit Verwendung von weiteren Bibliotheken/Modulen
# ist es auch möglich, definierte Zeitzonen einzurichten,
# die dann mit den entsprechenden Daten (insbesondere
# dem Time-Off-Set) gefüllt werden
Zeitzone = pytz.timezone('Asia/Calcutta')
Datum = datetime.datetime.now(Zeitzone)
print(Datum, Datum.strftime("%Z"))
print(Datum.isoformat())

Zeitzone = gettz("Australia/West")
Datum = datetime.datetime.now(Zeitzone)
print(Datum, Datum.strftime("%Z"))
print(Datum.isoformat())

# mit astimezone kann dann ein Datum umgewandelt werden
Datum = datetime.datetime.now()
print("vorher:", Datum)
Zeitzone = gettz("Australia/West")
Datum2 = Datum.astimezone(Zeitzone)
print("nachher:", Datum2)

# bei den Änderungen wurde gezeigt, daß mit replace Bestand-
# teile eines Datums geändert werden können
# das schließt auch die Zeitzone ein
from dateutil import tz

# Variante 1:
VonZone = tz.gettz('UTC')
ZuZone = tz.gettz('America/New_York')

# Variante 2:
# (zeigt auch weitere Möglichkeiten von dateutil)
VonZone = tz.tzutc()
ZuZone = tz.tzlocal()

UTC = datetime.datetime.utcnow()
# utc ist jetzt ein 'naives' Datum
# mit der nachfolgenden Anweisung wird die 
# Zeitzone 'bewußt' festgelegt
UTC = UTC.replace(tzinfo=VonZone)
print("UTC", UTC)

# jetzt kann die Konvertierung durchgeführt werden
Lokal = UTC.astimezone(ZuZone)
print("Lokal", Lokal)

# Warum aber ist das Ganze so wichtig?
# Wenn Daten international ausgetauscht werden, müssen die
# Empfänger die Zeiten (automatisiert) 'umrechnen' können
