class Fahrzeug:
    def __init__(self, m = None, nr = None, modell= None): # default kann überladen werden
        self.marke = m # Attribut / Feld
        self.fahrgestellnr = nr
        self.modell = modell

    def fahren(self): # Methode
        print(f"Der {self.marke} fährt")

    #factory methode
    @classmethod
    def from_string(cls, line):
        marke, fahrgestellnr, modell = line.split(",")
        return cls(marke, fahrgestellnr, modell)

f = Fahrzeug("BMW") # Instanzerstellung mittels Konstruktor
f.fahren()

f = Fahrzeug() # Instanzerstellung mittels Konstruktor
f.marke = "Audi"
f.fahren()

# lese csv zeilenweise
# erstele von jeder zeile ein objekt
fneu = Fahrzeug.from_string("Skoda,1234124312312,Octavia")
print(fneu.modell)
