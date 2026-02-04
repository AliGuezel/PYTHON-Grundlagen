#*****************************************************************
# Primzahlberechnung nach Sieb des Eratosthenes:
# schleifenbasierte Lösung:
noprimes = []
for i in range(2, 8):
    for j in range(i * 2, 100, i):
        noprimes.append(j)

primes = []
for x in range(2, 100):
    if x not in noprimes:
        primes.append(x)

print(primes)

# zwei Listenabstraktionen
noprimes = [j for i in range(2, 8) for j in range(i * 2, 100, i)]
primes = [x for x in range(2, 100) if x not in noprimes]
print(primes)

# geht auch als 'One-Liner':
primes = [x for x in range(2, 100) if x not in [j for i in range(2, 8) for j in range(i * 2, 100, i)]]
print(primes)

# Zeilenumbrüche sind dabei dann erlaubt:
primes = [x for x in range(2, 100) if x not in
          [j for i in range(2, 8) for j in range(i * 2, 100, i)]]
print(primes)

