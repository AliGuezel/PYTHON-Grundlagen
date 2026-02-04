# Die Besonderheiten des ASCII-Zeichensatzes
# haben zur Definition von speziellen Zeichenmengen
# im Modul string geführt:
import string

# Untermengen
print(string.whitespace)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.ascii_letters)

# z.B. ist das Zeichen eine Zahl:
print("5" in string.digits)

s = "What's wrong with ASCII?!?!?"
print(s.rstrip(string.punctuation))

# die eingebaute ascii-Funktion wandelt ein
# beliebiges object in einen ASCII-String um
# Nicht-ASCII-Zeichen werden in Escape-Se-
# quenzen umgewandelt
print(ascii("a"))
print(ascii("å"))