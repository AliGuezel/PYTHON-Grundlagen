def getGanzzahl(Anzeigetext = "Geben Sie eine Zahl ein: "):
    while True:
        Eingabe = input(Anzeigetext)
        if Eingabe.upper() == "B":
            return None
        try:
            Zahl = int(Eingabe)
            return Zahl
        except:
            print("Sie haben keine gültige Zahl eingegeben, B für Beenden oder eine gültige Zahl")

print(getGanzzahl())