# durch die Verwendung von Bedingungen kann der Code für
# die verflixte Sieben wie folgt umgeschrieben werden

Zahl = 1741

print(Zahl % 7)

Rest = Zahl 
LetzteZiffer = Rest % 10
if LetzteZiffer % 7 == 0:
    print("letzte Zahl ist eine 7")

Rest = Rest // 10
LetzteZiffer = Rest % 10
if LetzteZiffer % 7 == 0:
    print("vorletzte Zahl ist eine 7")

Rest = Rest // 10
LetzteZiffer = Rest % 10
if LetzteZiffer % 7 == 0:
    print("vorvorletzte Zahl ist eine 7")

# oder
Zahl = 1640

if Zahl % 7 == 0:
    print("Piiiep, die Zahl ist durch 7 teilbar")

else:

    LetzteZahl = Zahl % 10
    if LetzteZahl % 7 == 0:
        print("piiiep 7 enthalten")

    else:
        Zahl = Zahl // 10
        LetzteZahl = Zahl % 10
        if LetzteZahl % 7 == 0:
            print("piiiep 7 enthalten")

        else:
            Zahl = Zahl // 10
            LetzteZahl = Zahl % 10
            if LetzteZahl % 7 == 0:
                print("piiiep 7 enthalten")
                
            else:
                Zahl = Zahl // 10
                LetzteZahl = Zahl % 10
                if LetzteZahl % 7 == 0:
                    print("piiiep 7 enthalten")