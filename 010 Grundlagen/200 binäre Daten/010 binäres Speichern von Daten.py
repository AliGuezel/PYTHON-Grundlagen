# Bisher wurden die Daten als Textdaten gespeichert, Daten können
# aber auch im binärer Form gespeichert werden.
# Das Speichern in binärer Form hat zwei Vorteile: es ist schneller
# und sie brauchen weniger Platz.
# Der Nachteil ist, daß diese Daten nicht ohne weiteres austauschbar,
# vor allem nicht menschenlesbar sind.
#
# in Python müssen die Daten zunächst in binäre Daten umgewandelt
# werden, damit sie auch binär abgespeichert werden.
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

# encode bietet die Möglichkeit, Argumente
# für die Fehlerbehandlung anzugeben
s = "Dies ist ein Ströng"
s2 = s.encode("ascii", "ignore")
print(s2)

s = "Dies ist ein Ströng"
s2 = s.encode("ascii", "replace")
print(s2)


# Die Problematik mit Zeichen jenseits des ASCII-Zeichen-
# satzes ist auch der Grund dafür, daß es nicht einfach
# möglich ist, einen ByteArray mit strings zu erzeugen.

# Zahlen funktionieren ohne Erweiterungen
b = bytearray(42)
print(b, type(b))

b = bytearray([1, 2, 3])
print(b, type(b))

# Wenn nun die Datei binär umgewandelt sind, können sie auch so geschrieben
# und dann auch wieder gelesen werden:
f = open("D:/Tmp/binfile.bin","wb")
num = [5, 10, 15, 20, 25]
arr = bytearray(num)
f.write(arr)
f.close()

f = open("D:/Tmp/binfile.bin","rb")
num = list(f.read())
print(num)
f.close()


# jetzt entsteht allerdings ein Problem: wie können Strings binär gespeichert
# werden? Nachfolgende Zeile erzeugt einen Fehler:
# b = bytearray("Dies ist ein Text")
# print(b)

# Der Grund dafür ist, daß Python wissen muß, mit welchem Zeichensatz die
# Zeichenfolge codiert werden soll.
# Eine binäre Codierung erfolgt ja so, daß einem Buchstaben erst eine Zahl
# zugewiesen wird und dann wird diese Zahl binär codiert.
# Das Problem ist also: welcher Buchstabe bekommt welche Zahl und dies nennt
# man Zeichensatz. Der verwendete Zeichensatz muß gemerkt werden, damit aus
# den Zahl auch wieder die richtigen Texte (Buchstabenfolgen) werden.
b = bytearray("Dies ist ein Text", "ascii")
print(b)

# Ein weiteres Problem entsteht dann, wenn eine Zeichenfolge Zeichen enthält,
# die in dem angegebenen Zeichensatz nicht enthalten sind:
#print(bytearray("Öch weiß nöch, warum äch so traurig bön", "ascii"))
print(bytearray("Öch weiß nöch, warum äch so traurig bön", "utf-8"))

# wenn man nun einen ByteArray erzeugt hat, kann man Zeichenfolgen abspeichern,
# wie zuvor die Zahlen abgespeichert wurden.
f = open("D:/Tmp/binfile.bin","wb")
b = bytearray("Öch weiß nöch, warum äch so traurig bön", "utf-8")
f.write(b)
f.close()

# nach dem Lesen bekommt man natürlich erst mal einen ByteArray, auch hier
# muß also das Python-Programm für die Umwandlung sorgen und dabei dann
# angeben, welches Encoding (welcher Zeichensatz) verwendet werden soll.
f = open("D:/Tmp/binfile.bin","rb")
b = f.read()
s = b.decode("utf-8")
print(s)
f.close()

# auch beim Dekodieren muß ein passendes Encoding ein-
# gesetzt werden
s = "Dies ist ein Ströng"
s2 = s.encode()
print(s2.decode("ascii"))

# auch beim Dekodieren kann eine Fehlerbehandlung angegeben
# werden
s = "Dies ist ein Ströng"
s2 = s.encode()
print(s2.decode("ascii", "replace"))