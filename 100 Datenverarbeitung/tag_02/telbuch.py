telefonbuch = {
    "Ali": "1234",
    "Tom": "4321",
    "Micha": "5678",
    "Anja": "8765"
}
n = input("Name: ")

if n not in telefonbuch:
    print(telefonbuch.get(n, "Der Name ist nicht eingetragen"))
    add = input("Möchten Sie es eintragen? (/) ")
    if add == "J" or add == "J":
        neunum = input("Geben Sie die Nummer ein: ") 
        telefonbuch[n] = neunum
        print("Erfolgreich eingetragen")
        print('Das Telefonnummer von ' + n + ' ist ' + str(telefonbuch[n]))
else:
    print('Das Telefonnummer von ' + n + ' ist ' + str(telefonbuch[n]))