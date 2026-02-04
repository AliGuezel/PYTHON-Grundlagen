# Beispiel dafür, daß auch eine feststehende Quellmenge
# verwendet werden kann
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
print(Fahrenheit)



# ****** Verschachtelungen

# Schleifenbasierte Lösung
lst1 = ["A", "B", "C"]
lst2 = ["D", "E", "F", "G"]
erg = []
for s1 in lst1:
    for s2 in lst2:
        erg.append((s1, s2))
print(erg)

# mit ListComprehensions
lst1 = ["A", "B", "C"]
lst2 = ["D", "E", "F", "G"]
erg = [(a,b) for a in lst1 for b in lst2]
print(erg)

# *********** andere Sammlungstypen 

# Dictionaries
# wird in geschweifte Klammern gesetzt
# in jedem Schleifendurchlauf muß ein Schlüssel-Wert-Paar
# erzeugt werden

namen = ["Donald", "Dagobert", "Daisy", "Gustav"]
print({k:len(k) for k in namen})
print({k:len(k) for k in namen if k[0] == "D"})

lst1 = ["A", "B", "C"]
lst2 = [2, 4, 6]
print({k:[k*i for i in lst2] for k in lst1})

lst1 = ["Jan", "Feb", "Mrz"]
lst2 = [1, 2, 3]
erg = { Num : lst1[Num - 1] for Num in lst2 }
print(erg)

# Mengen (Sets), durch Verwendung der geschweiften Klammern
lst = [1,2,3,4,5,6,7,8,9]
erg = {i**2 for i in lst}
print(erg)
