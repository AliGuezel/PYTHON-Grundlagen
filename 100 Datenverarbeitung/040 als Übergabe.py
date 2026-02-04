# Datentypen wie Listen oder Dictionaries können auch verwendet werden,
# um zusammenhängende Daten an Funktionen zu übergeben
# Werden solche Datenzusammenhänge übergeben, bleiben Änderungen 'erhalten'
# das markiert einen wichtigen Unterschied zur Übergabe von z.B. Zahlen

# Der Unterschied ist die Übergabe als Wert (bei einfachen Werttypen)
# und als Referenz (bei Dictionaries oder Listen).
# Bei Zahlen wird eine Kopie der Daten übergeben, man bezeichnet diese
# Daten deshalb auch als Werttypen. Bei Wörterbüchern und Listen wird
# demgegenüber die Speicheradresse der Daten übergeben. Das Prinzip ist also:
# - Daten werden einer Variablen zugewiesen
# - die Variable beinhaltet die Adresse, an der die Daten liegen
# - diese Adresse wird an die Funktion weitergegeben
# - das bedeutet, die Funktion arbeitet mit den gleichen Daten
# - Änderungen an diesen Daten sind damit dann dauerhaft
def Tunen(PKW):
    PKW["PS"] = PKW["PS"] * 2

Autodaten = {
                "Kennzeichen" : "UN PP 900",
                "PS" : 90
            }
print(Autodaten)
Tunen(Autodaten)
print(Autodaten)

def Aendern(Wert):
    Wert = Wert * 2
    print(Wert)

Zahl = 10
print(Zahl)
Aendern(Zahl)
print(Zahl)

def Aendern(Zahl):
    Zahl[0] = Zahl[0] + 2

z = [3, ]
Aendern(z)
print(z[0])