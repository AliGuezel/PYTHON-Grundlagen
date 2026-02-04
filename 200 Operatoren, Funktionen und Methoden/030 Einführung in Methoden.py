# Bisher allgemeine Methoden wie z.B. print
# jetzt: Methoden, die mit einem bestimmten Datentyp verbunden sind
# also: wir haben einen String und mit dem ist eine Methoden verbunden,
# die auf den aktuellen String angewendet werden kann.
#
# Die allgemeine Syntax ist jetzt nicht mehr:   upper(<String>)
# sondern:                                      <string>.upper()
#
# Der Grund ist, daß es sich nicht um eine Methode handelt, die
# auch auf andere Datentypen angewendet werden kann, sondern um
# eine Methode, die mit dieser speziellen Zeichenfolge verbunden
# ist.
#
# Die Methode wird durch einen Punkt abgetrennt angehängt.
#
# In den meisten IDEs zeigt dann Intellisense, welche Methoden
# zur Verfügung stehen

print("in kleinbuchstaben geschrieben".upper())

s = "in kleinbuchstaben geschrieben"
print(s.upper())

s = "1234"
print(s.zfill(8))

s = "in kleinbuchstaben geschrieben"
print(s.count("i"))
print(s.count("i", 10))

