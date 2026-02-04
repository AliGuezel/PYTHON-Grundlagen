# einfache Krücke für das Slicing mit Dictionaries
# Übertrag aus Projekt Distionary
def DicSlice(Dictionary, Start, Stop, Step=None):
    SchluesselListe = list(Dictionary.keys())
    Auswahl = SchluesselListe[Start:Stop:Step]
    Ergebnis = {}
    for Element in Auswahl:
        Ergebnis[Element] = Dictionary[Element]
    return Ergebnis

d = {"A": "ABC", "D": "DEF", "G": "GHI",
     "J": "JKL", "M": "MNO", "P": "PQR"}
#print(DicSlice(d, 1, 3))

SliceObjekt = slice(2, 9)
Zeichenkette = "Gugelhupf"
#print(Zeichenkette[SliceObjekt])

# für später im Kontext OOP:
# beim Slicing wird der dunder __getitem__ aufgerufen
class Test:
    def __getitem__(self, val):
        print(type(val), val, val.start, val.stop, val.step)

t = Test()
t[3:4]
t[1::2]

class MeinDictionary(dict):
    # def __getitem__(self, val):
    #     SchluesselListe = list(super().keys())
    #     Auswahl = SchluesselListe[val.start:val.stop:val.step]
    #     Ergebnis = {}
    #     for Element in Auswahl:
    #         Ergebnis[Element] = super().__getitem__(Element)
    #     return Ergebnis
    def __getitem__(self, val):
        print(super().items())
        print(list(super().items()))
        return dict(list(super().items())[val.start:val.stop:val.step])

md = MeinDictionary()
md.update({"A": "ABC", "D": "DEF", "G": "GHI",
     "J": "JKL", "M": "MNO", "P": "PQR"})
print(md)
print(md[2:4])

d = {}
d.update({"A": "ABC", "D": "DEF", "G": "GHI",
          "J": "JKL", "M": "MNO", "P": "PQR"})
print(dict(list(d)[2:4]))