# komplette Hierarchie der Tiere
# die abgeleiteten Klassen rufen die Konstruktoren der 
# Basisklassen auf, dadurch werden die Attribute ein-
# gerichtet
class Tier:
    def __init__(self):
        self.Name = ""
    def Posen(self):
        print("ich pose, also bin ich")



class Raubtier(Tier):
    def __init__(self):
        super().__init__()
        self.Beute = ""

class Pflanzenfresser(Tier):
    def __init__(self):
        super().__init__()
        self.Grasmenge = 0.0



class Tiger(Raubtier):
    def __init__(self):
        super().__init__()
        self.StreifenArt = ""


class Gazelle(Pflanzenfresser):
    def __init__(self):
        super().__init__()
        self.Geschwindigkeit = 65.9

g = Gazelle()
g.Posen()
print(g.Grasmenge)
g.Grasmenge = 12.3
print(g.Grasmenge)
g.Alter = 10
print(g.Alter)

print([m for m in dir(Gazelle) if not m.startswith('_')])
print(g.__dict__)