# zu beachten ist, daß die Methoden, die mit einem String verbunden 
# sind, nicht den ursprünglichen String verändern:
Original = "zeichenfolge"
print(Original)
Original.upper()
print(Original)

# Lösung ist, das Ergebnis der Methode upper() 'aufzufangen'
Original = "zeichenfolge"
Kopie = Original.upper()
print("Original:", Original)
print("Kopie:", Kopie)


# Der Grundmechanismus, daß 
# K o p i e n   z u r ü c k g e g e g e b e n 
# werden, gilt für 
# a l l e    M e t h o d e n