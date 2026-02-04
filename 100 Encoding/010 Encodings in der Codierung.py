# Quellcode ist in Python UTF-8 codiert, weshalb es 
# möglich ist, Zeichen außerhalb des ASCII-Bereichs
# zu verwenden

# Für die Nicht-ASCII-Zeichen gibt es eine eigene PEP
# https://www.python.org/dev/peps/pep-3131/

# in einer Quellcode-Datei kann in der ersten (bzw.
# zweiten Zeile (Shebang: https://de.wikipedia.org/wiki/Shebang))
# die Zeichencodierung des Quellcodes angegeben werden,
# was aber nur Konsequenzen für den jeweiligen Codeeditor hat.
# Beispiel:
# -*- coding: utf-8 -*-
#
# PyCharm zeigt eine Warnung

Püthøn = "Test"
print(Püthøn)

