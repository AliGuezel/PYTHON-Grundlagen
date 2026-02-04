import pprint

Autoliste = {
                "A" :
                {
                    "Kennzeichen" : "UN PP 900",
                    "Motor" :
                    {
                        "PS" : 100,
                        "Hubraum" : 2000
                    }
                },
                "B" :
                {
                    "Kennzeichen" : "DO LL 123",
                    "Motor" :
                    {
                        "PS" : 75,
                        "Hubraum" : 1500
                    }
                }
            }

print(pprint.pformat(Autoliste))

Datei = open("D:/Tmp/Autoliste.txt", "w")
Datei.write("\n" + pprint.pformat(Autoliste) + "\n")
Datei.close()

