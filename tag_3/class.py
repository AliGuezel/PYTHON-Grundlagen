class Fahrzeug:
    def __init__(self, m = None): # default kann überladen werden
        self.marke = m # Attribut / Feld

    def fahren(self): # Methode
        print(f"Der {self.marke} fährt")

f = Fahrzeug("BMW") # Instanzerstellung mittels Konstruktor
f.fahren()

f = Fahrzeug() # Instanzerstellung mittels Konstruktor
f.marke = "Audi"
f.fahren()