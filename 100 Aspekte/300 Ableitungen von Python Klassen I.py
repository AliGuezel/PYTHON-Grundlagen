# ein weiterer sehr leistungsfähiger Zusammenhang ergibt sich dadurch,
# daß aus den Python-Klassen heraus eigene Ableitungen gebildet werden
# können.
# Damit können bestehende Klassen z.B. mit neuen, weiteren Methoden
# (oder Daten) auszustatten oder aber die Verwendung von Funktionalitäten
# zu erleichtern.
# Zu beachten ist dabei, daß eine eigene Klasse nach der Ableitung über
# alle Member der Basisklasse verfügt.
# Leitet man also z.B. eine eigene Klasse von der Klassen str (string) ab,
# können Objekte, die aus der eigenen Klasse gebildet werden, alles, was
# ein string(-Objekt) kann.

class MeinString(str):
    pass
s = MeinString("Gugelhupf")
print(s.upper())

# man kann dann die eigene Implementierung mit weiteren
# Methoden ergänzen, um z.B. mit bestimmten Gebrauchs-
# weisen zu erweitern
class MeinString(str):
    def EinzelneWoerter(self):
        return super().__str__().split(" ")

s = MeinString("Dies ist ein Text mit einzelnen Wörtern")
print(s.EinzelneWoerter())


# das Ersetzungsprinzip sorgt auch für die Möglichkeit, bestehende
# Implementierungen in einem Typ einfach mit eigenen auszutauschen:
class MeinString(str):
    def upper(self):
        return super().__str__().lower()

s = MeinString("Gummistiefel")
print(s.upper())