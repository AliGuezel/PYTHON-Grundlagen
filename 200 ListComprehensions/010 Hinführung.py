# Wie kann man aus einer Menge eine neue Menge erzeugen
# z.B. alle ungeraden Zahlen bis ausschließlich 10?

# mit einer Schleife
i = 0
Zahlen = []
while i < 10:
    if i % 2 == 1:
        Zahlen.append(i)
    i += 1
print(Zahlen)

# mit range
Zahlen = list(range(1, 10, 2))
print(Zahlen)

