# https://docs.python.org/3.8/library/locale.html

import datetime
import locale

# Python ist vom Standard her aud die US-amerikanische Kultur eingestellt,
# was sich zeigt, wenn man den Monatsnamen eines Datums verwendet
# (die Erklärung zur Methode folgt bei 'Darstellung')
Datum = datetime.date(2020, 7, 14)
print(Datum.strftime("%B"))

locale.setlocale(locale.LC_ALL, "")
print(Datum.strftime("%B"))

locale.setlocale(locale.LC_ALL, "en_US")
print(Datum.strftime("%B"))

# um die verwendete Kultur umzustellen, kann die Bibliothek locale
# verwendet werden
# setlocale stellt die Kultur um
# der 1. Parameter regelt den Umfang
# der 2. die Zielkultur
locale.setlocale(locale.LC_ALL, "de_DE")

print(Datum.strftime("%B"))

print(locale.getdefaultlocale())
print(locale.getlocale())

# über locale sind auch kulturspezifische Vergleiche durchzuführen
# strxfrm wandelt den String um
# strcoll gibt das Ergebnis des Vergleichs zurück:
# String1 ist kleiner (-1), gleich (0) oder größer (1) als String2
# zu beachten ist, daß an dieser Stelle im Beispielcode
# bereits auf die deutsche Kultur umgestellt ist!
print(locale.strxfrm("Strasse") == locale.strxfrm("Straße"))
print(locale.strcoll("Strasse", "Straße"))

x = 1234.45
print(locale.format_string("%.2f", x))
print(locale.format_string("%.2f", x, monetary=True))
print(locale.delocalize("1234,45"))

# erweitertes Beispiel
import locale

s1 = "Coté"
s2 = "coté"
s3 = "côte"

locale.setlocale(locale.LC_ALL, "fr_FR")
print(locale.strcoll(s1, s2))
print(locale.strcoll(s1, s3))
print(locale.strcoll(s2, s3))

locale.setlocale(locale.LC_ALL, "jp_JP")
print(locale.strcoll(s1, s2))
print(locale.strcoll(s1, s3))
print(locale.strcoll(s2, s3))

# es gibt eine Reihe von Methoden, die (unter Windows)
# nicht funktionieren
# locale.nl_langinfo()
# locale.resetlocale()
