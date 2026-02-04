# time ist das Modul mit der älteren, eher prozeduralen Variante,
# mit Datum und Zeit zu arbeiten
# Basis für dieses Modul ist die sogenannte Unix-Epoche, d.h. es
# werden die Sekunden nach dem 1.1.1970 gezählt, die abgerufen 
# werden können
#
# Um die einzelnen Anteile eines kompletten Datums (mit Zeit) verwalten
# zu können, gibt es eine entsprechende Datenstruktur: struct_time
#
# diese Struktur kann entweder über diverse Funktionen oder manuell,
# durch Übergabe der einzelnen Bestandteil erfolgen
import time

# Anzahl Sekunden nach 1.1.1970:
print("Gesamtzahl Sekunden:", time.time(), type(time.time()))

# seit der Version 3.7 ist es auch möglich, die Zeit in ns abzurufen:
print(time.time_ns())

Datum = time.ctime()
print(Datum)

# Erzeugung der struct_time Struktur:
Datum = time.localtime()
print(Datum)

# diese Datenstruktur stellt Attribute 
# für die Datumsanteile zur Verfügung
# Attribute sind schreibgeschützt
print(Datum.tm_year)
print(Datum.tm_mon)
print(Datum.tm_mday)
print(Datum.tm_hour)
print(Datum.tm_min)
print(Datum.tm_sec)
print(Datum.tm_wday)        # Wochentag, Montag = 0
print(Datum.tm_yday)        # Tag im Jahr
print(Datum.tm_isdst)       # an die Sommerzeit angepaßt, 0 = nein, ansonsten = ja

# ein Datum kann über die Struktur auch manuell eingerichtet werden:
Datum = time.struct_time((2020, 4, 9, 12, 34, 23, 0, 0, 0))
print(Datum)


# zu beachten ist bei dieser Variante, daß Strukturdaten wie z.B.
# Wochentag beibehalten werden
# Um also ein 'vollständig korrektes' Datum zu erhalten, müssen die
# zugehörigen Werte erst ermittelt und dann gesetzt werden
# (Der 9.4.2020 war ein Donnerstag!)
print(Datum.tm_wday)

