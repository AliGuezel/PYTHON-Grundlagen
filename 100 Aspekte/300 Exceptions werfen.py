# nachfolgende Funktion gaukelt auch bei Übergabe
# eines falschen (z.B. leeren) Kennzeichens vor, 
# daß 'die Welt in Ordnung' ist...
# z.B. auch für "UN CHIEN"
def IstKennzeichenAusUnna(Kennzeichen):
    return Kennzeichen[:2] == "UN"

# defensive Programmierung, aber der Aufrufer merkt
# nichts von der falschen Eingabe oder muß None aus-
# werten (wenn der unterste return-Zweig rausgenommen
# wird:
def IstKennzeichenAusUnna(Kennzeichen):
    if len(Kennzeichen) >= 5 and len(Kennzeichen) <= 10:
        return Kennzeichen[:2] == "UN"
    #return false


# in nachfolgender Version wird das Kennzeichen nur geprüft,
# wenn es an sich korrekt ist
# ist das Kennzeichen nicht korrekt, wird eine Ausnahme
# geworfen, auf die der Aufrufer entsprechend reagieren 
# kann (Ausschimpfen des Anwenders)
def IstKennzeichenAusUnna(Kennzeichen):
    if len(Kennzeichen) < 5 or len(Kennzeichen) > 10:
        raise ValueError("Das Kennzeichen hat ein falsches Format")
    return Kennzeichen[:2] == "UN"

try:
    print(IstKennzeichenAusUnna("UN"))
except ValueError:
    print("Mist gebaut")


# es ist in Python möglich, den Fehler 'einfach' zu erweitern
# und ihm weitere Daten zu spendieren, die der Aufrufer dann
# auswerten kann
def IstKennzeichenAusUnna(Kennzeichen):
    if len(Kennzeichen) < 5 or len(Kennzeichen) > 10:
        Fehler = ValueError("Das Kennzeichen hat ein falsches Format")
        Fehler.Kennzeichen = Kennzeichen
        raise Fehler
    return Kennzeichen[:2] == "UN"

try:
    print(IstKennzeichenAusUnna("UN"))
except ValueError as ex:
    print("Mist gebaut, Eingabe war: ", ex.Kennzeichen)
    
