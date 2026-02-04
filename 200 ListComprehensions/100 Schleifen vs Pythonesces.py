Liste = [1, 2, 3, 4]


# Old-School, C-Style Programmierung

erg = []
i = 0

while i < len(Liste):
    erg.append(Liste[i] * 2)
    i += 1
    
print(erg)

# erste Änderung ist der Rückgriff auf for

erg = []
for z in Liste:
    erg.append(z * 2)
print(erg)

# anstelle einer Schleife: ListComprehensions 
erg = [x * 2 for x in Liste]
print(erg)

