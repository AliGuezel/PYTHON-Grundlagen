# Strings sind in Python Unicode-basiert, d.h.
# in Strings können alle Unicode-Zeichen gespeichert
# werden.
# Die Zuweisung kann über die Escapesequenz \u, die
# Funktion chr (mit Hex-Zahlen) oder \N{Unicode-Name}
# erfolgen
# 
# eine der vielen Übersichten für Unicode-
# Bezeichnungen gibt es z.B. hier:
# https://www.sql-und-xml.de/unicode-database/

s = "\u20ac"
print(s)
s = "\N{euro sign}"
print(s)
s = "\N{snake}"
print(s)

# weitere Beispiele
print(chr(0x007B))
print(chr(0x2167))
print(chr(0x2168))
print(chr(0x1F600))
print(chr(0x1F609))

# alle Varianten sind natürlich äquivalent:
# a = 95 = 0x61
print((
        "a" ==
        "\x61" == 
        "\N{LATIN SMALL LETTER A}" ==
        "\u0061" ==
        "\U00000061"
    ))

# es ist auch möglich, sich Unicode-Zeichen mit weiteren
# Daten anzeigen/ausgeben zu lassen
# https://docs.python.org/3/library/unicodedata.html

import unicodedata

for i in range(0x2654, 0x2660):
    print(hex(i), chr(i), " - ", unicodedata.name(chr(i)))

