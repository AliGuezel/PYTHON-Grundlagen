# Bei der Umwandlung in binäre Daten wird die encode-
# Methode aufgeführt, die ohne weitere Angaben mit utf-8
# codiert.
# Es ist aber auch möglich, die Zeichencodierung explizit
# anzugeben, auch hier gilt: enthält der String ein Zeichen,
# welches nicht in der angegebenen Codierung enthalten ist,
# entsteht ein Fehler

s = "Gänseblümchen"
# print(s.encode("ascii"))
print(s.encode("utf-8"))

# encode bietet die Möglichkeit, Argumente
# für die Fehlerbehandlung anzugeben
s = "Dies ist ein Ströng"
s2 = s.encode("ascii", "ignore")
print(s2)

s = "Dies ist ein Ströng"
s2 = s.encode("ascii", "replace")
print(s2)

# die 'Rückgewinnung' erfolgt über die decode-Methode
s = "Dies ist ein String"
s2 = s.encode()
print(s2.decode())

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


