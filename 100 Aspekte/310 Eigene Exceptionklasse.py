# Theoretisch ist auch in Python möglich auch eigene Fehlerklassen
# durch Ableitung zu definieren

class KennzeichenFehler(ValueError):
    def __init__(self, Kennzeichen):
        super().__init__(f"Das Kennzeichen {Kennzeichen} hat das falsche Format")
        self.__Kennzeichen = Kennzeichen

    @property
    def Kennzeichen(self):
        return self.__Kennzeichen


# Fehler = KennzeichenFehler("BlubberBlubbBlubb")
# raise Fehler

try:
    raise KennzeichenFehler("Rosenstengel")
except KennzeichenFehler as e:
    print(e.Kennzeichen)


# Diese Variante dürfte in Python, obschon technisch möglich, aber kaum
# Anwendung finden. Der 'Zugewinn' im obigen Beispiel besteht ja ledig-
# lich darin, daß das fehlerhafte Kennzeichen gespeichert wird. Aber da
# Python ja ohnehin mit dynamischen und jederzeit beliebigen Daten ar-
# beitet, kann ja jederzeit die eingebaute Python-Klasse ValueError mit
# dem fehlerhaften Kennzeichen aufgefüllt werden.