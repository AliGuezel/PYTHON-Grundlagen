# ++++++++ Suchen +++++++++++

# ACHTUNG bei allen nachfolgenden Beispielen ist
# immer zu beachten, daß die Zeichenfolgen mit der
# Basis 0 indiziert ist
# Der erste Buchstabe hat also den Index 0
# der zweite Buchstabe hat den Index 1 usw.

s = "Mal sehen, wo das 'e' in diesem String vorkommt"
print(s.find("e"))

# es gibt weitere Varianten bei denen z.B. der Startindex
# angegeben werden kann und auch der End-Index
# ('bis hierhin und nicht weiter') kann angegeben werden
print(s.find("e", 15, 25))
print(s.rfind("e"))

# natürlich ist auch eine Suche mit einer Variablen möglich
Suchwort = "sehen"
print(s.find(Suchwort))

# wenn eine Zeichenfolge nicht gefunden werden konnte,
# wird bei find ein -1 zurückgegeben
print(s.find("Gugelhupf"))

# zu beachten ist, daß bei find (und auch bei index)
# Groß- und Kleinschreibung berücksichtigt wird
print(s.find("SEHEN"))

s = "Dieser String wird gleich durchsucht"
print(s.index("wird"))

# wird bei Index eine Zeichenfolge nicht gefunden, wird
# ein Fehler erzeugt
# print(s.index("nicht vorhanden"))

s = "Fischers Fritze fischt frische Fische"
print(s.count("sch"))


# ++++++++ Umwandeln +++++++++++

s = "Die Kinder spielen auf der Straße"

print(s.replace("Kinder", "Blagen"))
print(s.replace("i", "X", 2))

print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.capitalize())
print(s.casefold())
print(s.title())


# die zuvor beschriebenen Methoden sind wichtig für Vergleiche in Python:
print("ß".lower())
print("ß".upper().lower())

s1 = "Strasse"
s2 = "Straße"
s3 = "STRASSE"

print("einfach")
print(s1 == s2)
print(s1 == s3)
print(s2 == s3)

print("\nlower")
print(s1.lower() == s2.lower())
print(s1.lower() == s3.lower())
print(s2.lower() == s3.lower())

print("\ncasefold")
print(s1.casefold())
print(s2.casefold())
print(s3.casefold())

print(s1.casefold() == s2.casefold())
print(s1.casefold() == s3.casefold())
print(s2.casefold() == s3.casefold())


# ++++++++ Entfernen +++++++++++

s = " \t\n \r\tUmgeben von Whitespaces \t\t\r"
print(s.strip())
print(s.lstrip())
print(s.rstrip())

ziffern = "0123456789"
s = "3674784673546Versteckt zwischen Zahlen3425923935"
print(s.strip(ziffern))


# ++++++++ Ausrichten +++++++++++

s = "Richte mich aus"
print(s.center(50))
print(s.ljust(50))
print(s.rjust(50, "-"))


# ++++++++ Prüfen +++++++++++

s = "3244"
print(s.isdigit())
# weitere Prüfungen:
# - isalnum()
# - isalpha()
# - isdigit()
# - islower()
# - isupper()
# - isspace()
# - istitle()


# - s.startswith(prefix, [start, end])
# - s.endswith(suffix, [start, end])


# ++++++++ Auffüllen +++++++++++

s = "738"
s = s.zfill(16)
print(s)

