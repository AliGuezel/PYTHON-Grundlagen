import csv

class Fahrzeug:
    def __init__(self, marke, kennzeichen, bj) -> None:
        self.marke = marke
        self.kennzeichen = kennzeichen
        self.bj = bj
        self.fahrtenbuch = []
    
    def __str__(self) -> str:
        return f"{self.marke} {self.kennzeichen} ({self.bj})"

fahrzeuge = dict()
#fahrzeuge =  []

with open('fahrzeuge.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        fahrzeug_obj = Fahrzeug(row['MARKE'], row['KENNZEICHEN'], row['BJ'])
        #fahrzeuge.append(fahrzeug_obj)
        fahrzeuge[row['ID']] = fahrzeug_obj

for ## 
f = fahrzeuge['QW876']
f.fahrtenbuch.append()