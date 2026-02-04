z1 = 10
z2 = 20
z3 = 30
z4 = 40

# Bedingte Anweisungen können schnell sehr 'breit' werden
if z1 >= 10 and z2 <= 100 and z3 > 10 and z4 > 2:
    print("!")

# es ist in Python nicht möglich, einfach Zeilenumbrüche
# zu verwenden
#if z1 >= 10 
#    and z2 <= 100 
#    and z3 > 10 
#    and z4 > 2:
#    print("!")

# eine (unschöne, weil unleserliche) Variante ist, Zeilen-
# umbrüche mit einem Backslash einzuleiten
if z1 >= 10 \
    and z2 <= 100 \
    and z3 > 10 \
    and z4 > 2:
    print("!")

# es gibt aber auch die Möglichkeit, den gesamten Bedingungs-
# ausdruck einzuklammern und ihn dann umzubrechen
if (z1 >= 10 
    and z2 <= 100 
    and z3 > 10 
    and z4 > 2):
    print("!")
