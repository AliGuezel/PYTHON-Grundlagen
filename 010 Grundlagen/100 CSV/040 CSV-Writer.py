import csv

# newline ="" muß eingerichtet werden, da man sonst zwei Leerzeilen bekommt
# ; als delimiter, weil sonst Kommata verwendet werden
writer = csv.writer(open("D:/Tmp/autos.csv", "w", newline=""), delimiter=";")
writer.writerow(["marke", "modell", "leistung_in_ps"])

daten = (
            ["Volvo", "P245", "130"], 
            ["Ford", "Focus", "90"],
            ["Mercedes", "CLK", "250"], 
            ["Audi", "A6", "350"],
        )
writer.writerows(daten)


writer = csv.DictWriter(open("D:/Tmp/autos2.csv", "w", newline=""),
                        ["marke", "modell", "leistung_in_ps"], 
                        delimiter=";")
writer.writeheader()
daten = (
            {"marke" : "Volvo", "modell" : "P245",
            "leistung_in_ps" : "130"},
            {"marke" : "Ford", "modell" : "Focus",
            "leistung_in_ps" : "90"},
            {"marke" : "Mercedes", "modell" : "CLK",
             "leistung_in_ps" : "250"},
            {"marke" : "Audi", "modell" : "A6",
            "leistung_in_ps" : "350"})
writer.writerows(daten)