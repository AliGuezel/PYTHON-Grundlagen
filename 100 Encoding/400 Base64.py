# Quellcode:
# https://hg.python.org/cpython/file/2.7/Lib/base64.py
# https://realpython.com/cpython-source-code-guide/
#
# https://de.wikipedia.org/wiki/Base64
# https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/

import base64
 
#data = "Willibald Steinmetz liegt ruhig im Dornrößchenschlaf"
#encodedBytes = base64.b64encode(data.encode("utf-8"))
#encodedStr = str(encodedBytes, "utf-8")
#print(encodedStr)
#print(base64.decode())

DatenDekodiert = "Willibald Steinmetz liegt ruhig im Dornrößchenschlaf"

DatenBytes = DatenDekodiert.encode('utf-8')
Codiert = base64.b64encode(DatenBytes)
print(Codiert)
CodiertAnzeige = Codiert.decode('utf-8')
print(CodiertAnzeige)

DatenDekodiert = base64.b64decode(CodiertAnzeige)
print(DatenDekodiert)
DatenDekodiert = DatenDekodiert.decode("utf-8")
print(DatenDekodiert)
