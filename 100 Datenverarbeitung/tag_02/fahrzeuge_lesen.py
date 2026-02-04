import csv

class Fahrzeug:
    def __init__(self, marke, kennzeichen, bj) -> None:
        self.marke = marke
        self.kennzeichen = kennzeichen
        self.bj = bj
    
    def __str__(self) -> str:
        return f"{self.marke} {self.kennzeichen} ({self.bj})"

fahrzeuge = dict()

with open('fahrzeuge.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        fahrzeug_obj = Fahrzeug(row['MARKE'], row['KENNZEICHEN'], row['BJ'])
        fahrzeuge[row['ID']] = fahrzeug_obj

print(fahrzeuge['QW876'])