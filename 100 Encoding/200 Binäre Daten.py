# Unter Umständen müssen Zeichen binär codiert werden
# z.B. beim Austausch von Daten, beim binären Speichern
# etc.
# in Python gibt es dafür drei Möglichkeiten:
# - Voranstellen eines b vor einer Zeichenfolge
# - Erstellen eines ByteArrays
# - Verwenden der encode-Methode für strings

s = b"ein Text"
print(s)
s = "ein Text"
print(s.encode())

# Die vorstehenden Beispiele beinhalteten nur Zeichen
# aus dem ASCII-Zeichensatz, weshalb die Umwandlung ein-
# fach war, denn hier entsprechen sich Zeichen, 
# Zahl (Ordinalposition) und die Bit-Codierung für die Zahl

# was aber ist, wenn im String Zeichen enthalten sind, die
# nicht Teil des ASCII-Zeichensatzes ist

# Die einfache Form via b-Präfix erzeugt einen Fehler, weil
# diese Variante nur mit ASCII-Zeichen funktioniert 
#s = b"Gänseblümchen"
#print(s)

# bei Verwendung von encode gibt es keinen Fehler, weil
# encode vom Standard her mit der utf-8-Codierung ar-
# beitet, anstelle der Umlaute erscheinen deshalb
# merkwürdige Zeichenzusammenstellungen:
# G\xc3\xa4nsebl\xc3\xbcmchen
s = "Gänseblümchen"
print(s.encode())


# Die Problematik mit Zeichen jenseits des ASCII-Zeichen-
# satzes ist auch der Grund dafür, daß es nicht einfach
# möglich ist, einen ByteArray mit strings zu erzeugen.
# Zahlen funktionieren ohne Erweiterungen
print(bytearray(42))
print(bytearray([1, 2, 3]))

# bei strings aber wird ein Fehler erzeugt, weil das
# encoding, also die Angabe darüber fehlt, wie (also
# mit welchen Zahlenwerten) die Nicht-ASCII-Zeichen
# codiert werden sollen
# print(bytearray("ein Text"))
print(bytearray("ein Text", "utf-8"))

# wählt man nun einen Zeichensatz, der nicht 'paßt',
# d.h. in dem die Zeichen eines Strings nicht vor-
# kommen, entsteht ein entsprechender Fehler
print(bytearray("ein Text", "ascii"))
#print(bytearray("Öch weiß nöch, warum äch so traurig bön", "ascii"))
print(bytearray("Öch weiß nöch, warum äch so traurig bön", "utf-8"))

# eine binäre Zeichenfolge kann direkt, ohne Angabe des
# Encoding, mit einem ByteArray verarbeitet werden, denn der 
# kann ja nur aus ASCII-Zeichen bestehen:
s = b"ein Text"
print(bytearray(s))

