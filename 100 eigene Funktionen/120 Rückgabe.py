# return bedeutet immer den Ausstieg aus der Funktion
# nachfolgend formulierter Code wird nie ausgeführt
def Rueckgabe():
    return "Irgendein Text"
    print("Dieser Text wird niemals ausgegeben")
print(Rueckgabe())

# es ist möglich, daß eine Funktion nur in bestimmten
# Fällen einen Wert zurückgibt
# in den übrigen Fällen ist der Rückgabewert dann None
def TextErmittlung(Zahl):
    if Zahl % 2 == 0:
        return "Gerade"
print(TextErmittlung(3))

# enthält eine Funktion keine Rückgabe via return,
# wird automatisch None zurückgegeben
def KeineRueckgabe():
    print("Ausführung der Funktion")
print(KeineRueckgabe())

# es ist auch möglich, nur ein return anzugeben, was 
# ebenfalls ein None erzeugt
def EinfachesReturn():
    return
print(EinfachesReturn())

# Funktionen können auch mit pass 'entschärft' werden
def KeinCode():
    pass
print(KeinCode())

# Funktionen können auch mehrere Werte zurückgeben,
# die dann vom Aufrufer entpackt werden können
def Tauschen(Wert1, Wert2):
    return Wert2, Wert1
Erg1, Erg2 = Tauschen(2, 42)
print(Erg1, Erg2)

# Fehlerquelle:
# da es keinerlei Typprüfung gibt, kann eine Funktion
# auch None zurückgeben, welches vom Aufrufen fehl-
# haft weiterverarbeitet wird
def GeradeZahlZurueckgeben(Zahl):
    return Zahl if Zahl % 2 == 0 else None

erg = GeradeZahlZurueckgeben(2)
print(erg + 2)
erg = GeradeZahlZurueckgeben(3)
# erzeugt einen Fehler
# print(erg + 2)
# Lösung:
if erg != None:
    print(erg + 2)

# es ist möglich, eine bedingte Anweisung zu verwenden
def IstZahlGerade(Zahl):
    return True if Zahl % 2 == 0 else False
print(IstZahlGerade(8))
print(IstZahlGerade(5))
