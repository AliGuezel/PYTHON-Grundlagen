def getGanzzahl(Anzeigetext = "Geben Sie eine Zahl ein: "):
    while True:
        Eingabe = input(Anzeigetext)
        if Eingabe.upper() == "B":
            return None
        try:
            Eingabe = int(Eingabe)
            return Eingabe
        except ValueError:
            print("Sie haben keine gültige Zahl eingegeben, B für Beenden oder eine gültige Zahl")
        # except Exception:
        #     print("es ist ein unbekannter Fehler aufgetreten")

print(getGanzzahl())