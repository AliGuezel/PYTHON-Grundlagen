hersteller = "default"
fahrzeugbezeichnung = "default"
pss = 0
sitze = 0
hoechstgeschwindigkeit = 0
enterAnotherVehicle = True

fahrzeugListe = []

while enterAnotherVehicle:
 inputHersteller = input("Hersteller: ")
 if type(inputHersteller) is str:
  hersteller = inputHersteller
 else:
  print("Wert ist kein Text. Bitte nur Buchstaben eingeben.")
 break

 inputFahrzeugbezeichnung = input("Fahrzeugbezeichnung: ")
 if type(inputFahrzeugbezeichnung) is str:
  fahrzeugbezeichnung = inputFahrzeugbezeichnung
 else:
  print("Wert ist kein Text. Bitte nur Buchstaben eingeben.")
 break
 try:
  inputPss = int(input("PS: "))
 if type(inputPss) is int:
  pss = inputPss
 except ValueError:
 print("Wert ist keine Zahl. Bitte nur Zahlen eingeben.")
 break

 try:
  inputSitze = int(input("Sitze: "))
 if type(inputSitze) is int:
  sitze = inputSitze 

except ValueError:
print("Wert ist keine Zahl. Bitte nur Zahlen eingeben.")
 break

 try:
  inputHoechstgeschwindigkeit = int(input("Höchstgeschwindigkeit: "))
 if type(inputHoechstgeschwindigkeit) is int:
         hoechstgeschwindigkeit = inputHoechstgeschwindigkeit
 except ValueError:
 print("Wert ist keine Zahl. Bitte nur Zahlen eingeben.")
 break

 fahrzeugTuple = (hersteller, fahrzeugbezeichnung, pss, sitze, hoechstgeschwindigkeit)
 fahrzeugListe.append(fahrzeugTuple)

 inputAnotherVehicle = input("Weiteres Fahrzeug eingeben? (y/n): ")
 if inputAnotherVehicle == "y":
  enterAnotherVehicle = True
 continue 
 elif inputAnotherVehicle == "n":enterAnotherVehicle = False
 break


 def listenAusgabe():
  print("+------------+---------------------+-----+--------------+---------------------+")
 print("+ Hersteller + Fahrzeugbezeichnung + PS + Anzahl Sitze + Höchstgeschwidkeit +")
 print("+------------+---------------------+-----+--------------+---------------------+")

 i = 0
 for z in fahrzeugListe:
  print("+ " + fahrzeugListe[i][0] + " + " + fahrzeugListe[i][1] + " + " + str(fahrzeugListe[i][2]) + \
 " + " + str(fahrzeugListe[i][3]) + " + " + str(fahrzeugListe[i][4]) + " +")
 print("+------------+---------------------+-----+--------------+---------------------+")
 i += 1

 listenAusgabe()