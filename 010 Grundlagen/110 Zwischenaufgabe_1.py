# Wie sähe eine differenzierte Ausnahmebehandlung für den 
# nachfolgenden Code aus

while True:

    Zahlen = [1, 2, 3, 4, 5]
    print(Zahlen)

    Auswahl = input("Geben Sie den Index der gewünschten Zahl an: ")
    Index = int(Auswahl)
    Zahl = Zahlen[Index]
    print(Zahl)

    Multiplikand = int(input("Geben Sie den Multiplikanden ein: "))

    Schluessel = input("Geben Sie einen Schlüssel an, mit dem das Ergebnis gespeichert werden soll. ")

    Sammlung = { Schluessel: Zahl * Multiplikand }
    print(Sammlung)

    Schluessel = input("Welches Ergebnis soll angezeigt werden (Schlüssel)? ")
    print(Sammlung[Schluessel])
    
    if input("Weiter (J/N) ").upper() == "N":
        break



# nachfolgend sind einige Ausnahmebehandlungen zusammengefaßt
# Bringen Sie die jeweiligen Behandlungen in den Blöcken in eine
# sinnvolle Reihenfolge

# except OSError
# except FileExistsError
# except PermissionError
# except GeneratorExit

# except OverflowError
# except ArithmeticError
# except EOFError
# except MemoryError

# except ArithmeticError
# except OSError
# except AssertionError
# except ValueError

# except IndexError
# except LookUpError
# except FileNotFoundError
# except KeyError


# ************* Lösung

# except FileExistsError
# except PermissionError
# except OSError
# except GeneratorExit

# except OverflowError
# except ArithmeticError
# except EOFError
# except MemoryError

# except ArithmeticError
# except OSError
# except AssertionError
# except ValueError

# except IndexError
# except KeyError
# except LookUpError
# except FileNotFoundError
