## jedes 2. Element extrahieren
price = [
            [9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
            [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
            [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
            [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]
        ]

# schleifenbasierte Lösung
Ergebnis = []
for SubListe in price:
    Index = 0
    for Zahl in SubListe:
        if Index % 2 == 0:
            Ergebnis.append(Zahl)
        Index += 1
print(Ergebnis)

# vereinfachte schleifenbasierte Lösung
Ergebnis = []
for SubListe in price:
    for Zahl in SubListe[::2]:
        Ergebnis.append(Zahl)
print(Ergebnis)

# mit Listenabstraktion
sample = [line[::2] for line in price]
print(sample)