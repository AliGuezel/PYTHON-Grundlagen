# Da die Fehlerbehandlung jetzt spezifiziert ist, kommt
# es auf den Fehler an, welche Ausnahmebehandlung ver-
# wendet wird:
# - bei einer Eingabe von 0 kommt die Behandlung der
#   obersten Ebene zum Tragen
# - bei Eingabe einer Zeichenfolge wirkt die Behandlung
#   in der mittleren Ebene

def Berechnen(Zahl):
    return 42 / Zahl
       
def ZahlErmitteln():
    try:
        return Berechnen(int(input("Geben Sie eine Zahl ein: ")))
    except ValueError:
        print("Fehler in ZahlErmitteln")

try:
    print(ZahlErmitteln())
except ZeroDivisionError:
    print("Fehler im Programm")

