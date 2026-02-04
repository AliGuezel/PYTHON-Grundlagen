# es ist möglich, eine Hierarchie vonn Vererbungen über
# mehrere Ebenen einzurichten. Der Grundmechanismus bleibt
# derselber: eine abgeleitete Klasse erbt alle Member ihrer
# Basisklasse. Dies kaskadiert über alle Ebenen hinweg.
# Angenommen es gibt folgende Vererbungsreihenfolge
# KlasseA -> KlasseB -> KlasseC
# dann übernimmt KlasseC nicht alle Member der KlasseB
# da KlasseB aber alle Member der KlasseA übernommen hat,
# übernimmt KlasseC automatisch immer auch alle Member
# der KlasseA, d.h.
# KlasseC = KlasseA + KlasseB
class BasisKlasse:
    def MethodeDerBasisklasse(self):
        print("in der Basisklasse")

class Ableitung(BasisKlasse):
    def MethodeDerAbleitung(self):
        print("in der Ableitung")

class AbleitungDerAbleitung(Ableitung):
    def MethodeInDerAbleitungDerAbleitung(self):
        print("in der Ableitung der Ableitung")

a = AbleitungDerAbleitung()
a.MethodeDerBasisklasse()
a.MethodeDerAbleitung()
a.MethodeInDerAbleitungDerAbleitung()

print([m for m in dir(AbleitungDerAbleitung) if not m.startswith("_")])

# Wichtig: alle bisher aufgeführten Systematiken betreffen auch die
# Vererbung über mehrere Hierachieebenen. Eine Methode einer der Basis-
# klassen kann z.B. durch eine gleichnamige Methode einer Klasse irgendwo
# in der Hierarchie ersetzt werden
class BasisKlasse:
    def MethodeDerBasisklasse(self):
        print("in der Basisklasse")

class Ableitung(BasisKlasse):
    def MethodeDerAbleitung(self):
        print("in der Ableitung")

class AbleitungDerAbleitung(Ableitung):
    def MethodeDerBasisklasse(self):
        print("in der Ableitung der Ableitung, Basisklassen-Methode wurde ersetzt")

a = AbleitungDerAbleitung()
a.MethodeDerAbleitung()
a.MethodeDerBasisklasse()


# auch der Aufruf der Methoden der Basisklassen ist über mehrere Ebenen
# (zurück) möglich; Python wandert die Hierarchie rückwärts durch, bis
# es eine Methode mit dem angeforderten Namen findet
class BasisKlasse:
    def MethodeDerBasisklasse(self):
        print("in der Basisklasse")

class Ableitung(BasisKlasse):
    def MethodeDerAbleitung(self):
        print("in der Ableitung")

class AbleitungDerAbleitung(Ableitung):
    def MethodeDerBasisklasse(self):
        print("in der Ableitung der Ableitung")

a = AbleitungDerAbleitung()
a.MethodeDerAbleitung()
a.MethodeDerBasisklasse()
