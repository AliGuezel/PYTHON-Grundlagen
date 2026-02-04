# https://de.wikipedia.org/wiki/Mehrfachvererbung
# https://de.wikipedia.org/wiki/Diamond-Problem

# anstelle einer Hierarchie (die die Bezüge der Klassen
# senkrecht anordnet), ist es in Python auch möglich, eine
# Mehrfachvererbung zu implementieren.
#
# Ein Pferd beispielweise kann in einem bestimmten Programm
# gleichzeitig als ein Bauernhoftier und ein Zirkustier ein-
# gesetzt werden. Das ergibt aber keine Hierarchie, denn ein
# Zirkustier ist nicht sinnvollvon einem Bauernhoftier abzu-
# leiten, denn dann würde das Zirkustier ja alle Member des
# Bauernhoftieres erben. Genausowenig kann umgekehrt ein Bauern-
# hoftier von einem Zirkustier abgeleitet werden.
# Ein Pferd ist also beides, ein Bauernhoftier und ein Zirkustier,
# ohne daß Zirkustier und Bauernhoftier in irgendeinem (Vererbungs-
# zusammenhang stünden).
#
# Deshalb wird ein Pferd einfach von beiden Basisklassen abgeleitet.
class Zirkustier:
    def Posen(self):
        print("Posen")

class Bauernhoftier:
    def Arbeiten(self):
        print("Arbeiten")

class Pferd(Zirkustier, Bauernhoftier):
    pass

p = Pferd()
p.Posen()
p.Arbeiten()

# Ein Problem entsteht aber dann, wenn beide Basisklassen
# gleichnamige Methoden beinhalten - welche gilt dann?
# Python löst dies über MRO (Method Resolution Order), das
# bedeutet, es wird die Methode jener Klasse verwendet, die
# in der Angabe der Basisklasse am Anfang aufgeführt wurde.
class Tier:
    def Posen(self):
        print("Posen")

class Raubtier(Tier):
    def Posen(self):
        print("Zähnefletschen")

class Fisch(Tier):
    def Posen(self):
        print("schwimmen")

class HammerHai(Raubtier, Fisch):
    pass

class KragenHai(Fisch, Raubtier):
    pass

h = HammerHai()
h.Posen()
h = KragenHai()
h.Posen()
