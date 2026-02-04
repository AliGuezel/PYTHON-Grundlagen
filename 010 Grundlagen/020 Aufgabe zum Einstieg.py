# Nachfolgender Code macht Folgendes:
# - Zahlen werden in einer Liste gespeichert
# - der Benutzer kann auswählen, welche Zahl er verwenden möchte (= Indexauswahl)
# - der Benutzer kann anschließend die Zahl angeben, mit der die
#   zuvor ausgewählte Zahl multipliziert werden soll
# - der Benutzer kann dann einen Schlüssel angeben, mit dem das
#   Ergebnis der Multiplikation in dem Wöterbuch/Dictionary gespeichert werden soll
# - schließlich soll der Benutzer den Schlüssel für das Ergebnis angeben,
#   das er sich noch mal anschauen möchte

# Es sollen nun alle Stellen identifiziert werden, an denen eine Ausnahme-
# behandlung eingebaut werden sollte.
# Es genügt, die Stelle zu markieren, die Ausnahmebehandlung selbst
# muß nicht implementiert werden

while True:

    Zahlen = [10, 20, 30, 400, 57]
    print(Zahlen)

    Auswahl = input("Geben Sie den Index der gewünschten Zahl an: ")
    Index = int(Auswahl)
    Zahl = Zahlen[Index]
    print(Zahl)

    Multiplikand = int(input("Geben Sie den Multiplikanden ein: "))

    Schluessel = input("Geben Sie einen Schlüssel an, mit dem das Ergebnis gespeichert werden soll. ")

    Sammlung = { Schluessel: Zahl * Multiplikand }
    print(Sammlung)

    Schluessel = input("Welches Ergebnis soll angezeigt werden (Schlüssel)? ")
    print(Sammlung[Schluessel])
    
    if input("Weiter (J/N) ").upper() == "N":
        break



