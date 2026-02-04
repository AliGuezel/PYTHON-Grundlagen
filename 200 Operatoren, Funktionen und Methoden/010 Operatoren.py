# Einige der Operatoren, die im Zusammenhang mit Zahlen behandelt
# wurden, können auch im Zusammenhang mit Strings verwendet werden

# Verkettungen, auch als String-Konkatenation bezeichnet
Vorname = "Heinrich"
Nachname = "Müller"
Name = Vorname + " " + Nachname
print(Name)

# das allerdings erzeugt einen Laufzeitfehler:
s = "41"
z = s + 1

# es funktioniert erst durch explizite Typumwandlung
# eigentlich bekannt durch input (vorherige Lektion)
s = "41"
z1 = int(s)
z2 = z1 + 1

s = "Musik"
t = "lautsprecher"
s += t
print(s)

# Wiederholung von Sequenzen
print(3 * "abc")

Text = "bla"
Text *= 3
print(Text)

# Vergleich
s = "a"
t = "k"
s == t
s != t
s < t
s > t

# ACHTUNG:
# 1. es wird zwischen Groß- und Kleinschreibung unterschieden
s = "A"
t = "a"
s == t

# 2. es wird auf Basis der ASCII-Werte verglichen
"Zoo" < "merkwürdig"

# in = zusätzlicher Operator, der bei den Zahlen nicht 
# vorhanden war
Buchstaben = "abcdefghijklmnopqrstuvwxyz"

# Prüfen ob ein Element in der Sequenz enthalten ist
# zu beachten ist, daß die Zeichen case-sensitiv
# verglichen werden, d.h. K ist nicht gleich k
print("def" in Buchstaben)
print("def" in Buchstaben)
print("kLm" in Buchstaben)
print("KLM" not in Buchstaben)
print(not("XYZ" in Buchstaben))

