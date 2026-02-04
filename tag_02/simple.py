class Person: # Klasse
    def __init__(self, v, n): # Konstruktor mit Übergabeparantern
        self.vorname = v # Attribut
        self.nachname = n
    
    def getfullname(self): # Methoden
        return self.vorname + " " + self.nachname

    def __str__(self):
        return self.getfullname();

    def __repr__(self):
        return self.getfullname();

   # def __eq__(self, __o: object) -> bool:
   #     pass

class Mitarbeiter(Person):
    def __init__(self, v, n, nr): # Konstruktor mit Übergabeparantern
        super().__init__(v, n)
        self.personalnummer = nr
    
    def getfullname(self):
        return super().getfullname() + " (" + str(self.personalnummer) + ")"

m1 = Mitarbeiter("Hans", "Meier", 123)
#print(m1.getfullname())
#print(m1)

p1 = Person("Peter", "Pan")
p2 = Person("Peter", "Pan")
#print(p1.getfullname())
print(p1 == p2)


