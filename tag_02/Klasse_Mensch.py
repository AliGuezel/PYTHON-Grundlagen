class Person: # Klasse
    def __init__(self) -> None: # Konstruktor mit Übergabeparantern
        self.vorname = "" # Attribut
        self.nachname = ""

        def getfullname(self): # Methoden
            return self.vorname + " " + self.nachname

hans = Person("Hans", "Meier")
print(hans.getfullname()) # Zugriff
