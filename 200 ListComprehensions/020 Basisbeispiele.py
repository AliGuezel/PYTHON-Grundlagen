
# alle Zahlen aus einem Tupel in eine Liste übernehmen
Zahlen = [Zahl for Zahl in (1, 2, 3, 4)]
print(Zahlen)

# alle Zahlen aus einem Range-Objekt übernehmen
Zahlen = [Zahl for Zahl in range(10)]
print(Zahlen)

# Wert verändern
Zahlen = [Zahl * 2 for Zahl in range(10)]
print(Zahlen)

# Werte filtern
Zahlen = [x * 2 for x in range(10) if x % 2 == 1]
print(Zahlen)

