# Frage (Komplikation) 1:
# Wenn einer Funktion ein Wert übergeben wird
# und ändert diese Funktion den Wert, bleibt dann
# die Änderung auch im Aufrufer erhalten?
#
# Antwort: nein!
#
# Die Änderung eines übergebenen Wertes bleibt lokal
# begrenzt, der Aufrufer arbeitet mit den ursprüngli-
# chen Werten weiter.
#
#
# übergebene Variable wird in aufgerufener Funktion verändert
# diese Änderung bleibt aber nicht im Aufrufer bestehen
# Übergabe findet per value (als Wert) statt
# und nicht per ref (Referenz)
# Anders als in anderen Programmiersprachen gibt es in
# Python keine 'einfache' Möglichkeit, Daten per Referenz
# zu übergeben.
def Aenderung(ZahlInAufgerufenerFunktion):
    print(ZahlInAufgerufenerFunktion)
    ZahlInAufgerufenerFunktion = 10
    print(ZahlInAufgerufenerFunktion)

ZahlImAufrufer = 39
print(ZahlImAufrufer)
Aenderung(ZahlImAufrufer)
print(ZahlImAufrufer)
