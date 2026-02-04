# Umwandlungen von einem Sammlungstyp in einen anderen,
# um Grundcharakteristika zu verändern. Dabei wird der
# Zieldatentyp gewissermaßen als Funktion verwendet.
# Z.B. kann damit eine unveränderliche Liste (tuple) in
# eine veränderliche Liste (list) umgewandelt werden;
# Über set() kann eine eindeutige Sammlung erzeugt werdenn

# Zusammenstellung wird unveränderlich
Liste = [1, 2, 3, 4, 5]
Liste[2] = 666
Tupel = tuple(Liste)
# Fehler
# Tupel[2] = 3

# Zusammenstellung wird (umgekehrt) veränderlich
Zahlen = range(10)
# Fehler
# Zahlen[5] = 666
Liste = list(Zahlen)
Liste[5] = 666

# Zusammenstellung wird eindeutig
Liste = [1, 1, 1, 2, 2, 2, 3, 3, 3 ]
s = set(Liste)
print(s)
