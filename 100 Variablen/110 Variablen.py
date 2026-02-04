# Eine Variable wird einfach definiert 
# und ihr wird ein Wert zugewiesen
a = 41

# anschließend kann man das, was in der Variablen
# gespeichert ist, verwenden
print(a)
b = a + 1
print(b)

c = b
print(c)


# ********************************* Typisierung

# anders als in anderen Programmiersprachen wird
# der Typ der Variablen nicht definiert, der Typ
# wird von Python aus der Zuweisung abgeleitet.
Zahl = 9
# der Typ, den Python ermittelt hat, kann abgefragt werden:
print(type(Zahl))

# Deshalb MUSS eine Zuweisung erfolgen.
# Folgende Anweisungen führen deshalb zu einem
# Laufzeitfehler
d
print(d)

# ein weiterer Unterschied besteht darin, daß Python
# nicht mit statischer Typisierung arbeitet (da ja kein
# Typ vom Programmierer festgelegt wird).
# Einer Variablen kann dementsprechend zunächst eine
# Ganzzahl und dann im weiteren Verlauf eine Fließkomma-
# zahl zugewiesen werden:
Zahl = 90
print(type(Zahl))
Zahl = 9.9
print(type(Zahl))

# Zwar wird der Typ nicht im Code festgelegt, aber intern
# findet dennoch eine Typisierung statt. Python leitet den
# Typ aus der Zuweisung ab. Deshalb muß eine Typisierung
# vor der Verwendung erfolgen.
# Beispielsweise ist für Zeichenketten keine Subtraktion
# erlaubt
print("ABC" - "C")

# Dementsprechend sind folgende Anweisungen erlaubt, weil
# Python erkennt, daß es sich um
# Ganzzahlen handelt
Zahl1 = 10
Zahl2 = 5
erg = Zahl1 - Zahl2
print(erg)

# nachfolgende Anweisungen hingegen sind nicht erlaubt
Zeichenkette1 =" ABC"
Zeichenkette2 = "C"
erg = Zeichenkette1 - Zeichenkette2
print(erg)

# Damit Python prüfen kann, ob nachfolgende Operationen er-
# laubt sind, muß vorher der Typ festgelegt werden, was in
# Python durch Zuweisung von Werten geschieht.
# Deshalb kann Python nicht mit undefinierten Variablen ar-
# beiten
Irgendetwas1
Irgendetwas2
IrgendeinErgebnis = Irgendetwas1 - Irgendetwas2


# ********************************* Bezeichnungsregeln
# erlaubte Bezeichner:
Zahl = 90
Zahl1 = 90
Zahl_1 = 90

# führende oder schließende Unterstriche haben in Python eine
# besondere Bedeutung und sollten deshalb in 'normalen' Pro-
# grammierungen nicht verwendet werden
_Zahl = 90
Zahl_ = 90

# erlaubt, aber ungeeignet
ziqwezurziwuerziu = 90
Gügelhüpf = 90

# nicht erlaubt
# 1_Zahl = 90
# Z§ahl = 90
# Z ahl = 90
# class = 89

# zu beachten ist, daß Python case-sensitiv ist, d.h. für
# Python sind 'Zahl' und 'zahl' zwei verschiedene Bezeichnungen,
# was zu schwer zu findenden Fehlern führen kann
Zahl = 7
zahl = 9
print(Zahl)
print(zahl)


