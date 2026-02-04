# Tupel haben den Nachteil, daß sie unveränderlich sind,
# so daß immer eine feste Zusammenstellung entsteht
# Díes kann durch Verwendung von Listen geändert werden:

Auto1 = ["UN PP 900", 90, 2000]
Auto2 = ["DO KK 874", 75, 1500]
Auto3 = ["BO GF 534", 80, 1200]
Auto4 = ["DU YF 537", 60, 1000]

# Zusammenstellen zu einer Liste
Autoliste = [ Auto1, Auto2, Auto3, Auto4 ]
print(Autoliste)

# Alternative: mit einer leeren Liste beginnen...
Autoliste = []
print(Autoliste)
# anfügen ...
Autoliste.append(Auto1)
Autoliste.append(Auto2)
Autoliste.append(Auto3)
print(Autoliste)

# ... oder ...
Autoliste.clear()
print(Autoliste)
Autoliste.extend([Auto1, Auto4])
print(Autoliste)

PS = 1
# Veränderung einzelner Daten eines Autos
Autoliste[0][PS] = 200
print(Autoliste)