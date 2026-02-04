# Normalerweise wird einer Funktion eine definierte
# Anzahl an Argumenten übergeben
def Funktion(Zahl):
    print(Zahl)

Funktion(8)

# Funktionen können aber auch eine unbestimmte Zahl
# an Parametern vorsehen
# Eine Möglichkeit ist die Verwendung einer Sammlung
# zu beachten ist, daß immer nur ein Argument übergeben
# wird, welches zwar eine Sammlung darstellt, aber eben
# nur ein Argument ist.
def Funktion(Zahlen):
    for Zahl in Zahlen:
        print(Zahl, end = ' ')
Funktion((1, 2, 3,))
Funktion([1, 2, 3])
Funktion({1 : "A", 2 : "B", 3 : "C"})


# Was aber, wenn einer Funktion eine unbestimmte Anzahl
# übergeben werden soll - ein Beispiel dafür wäre etwa
# die Funktion print.
# Eine solche 'variadische' Funktion wird in Python auch
# wieder durch einen Astriks gekennzeichnet. Intern werden
# dann alle übergebenen Argumente in einen tuple umgewan-
# delt.
def Funktion(*args):
    print(type(args), args)
    for x in args:
        print(x)
Funktion(1, 2, 3)
Funktion(42)
Funktion()

# eine zweite Möglichkeit, in Python eine beliebige Anzahl
# an Argumenten zu übergeben, besteht in der Definition sog.
# Keyword-Args.
# Der Funktion wird dann eine Sammlung mit Schlüssel-Wert-
# Paaren übergeben, die Python in ein Dictionary umwandelt.
# Der Vorteil besteht dann darin, daß über den jeweiligen
# Schlüssel auf die übergebenen Daten zugegriffen werden
# kann,was die Zuordnung der Daten ein wenig 'zuverlässiger'
# macht.
def Funktion(**kwargs):
    print(type(kwargs), kwargs)
    for x in kwargs.items():
        print(x)

Funktion(a="A", b="B", c="C")


# Die eine Richtung ist also, daß einer Funktion eine be-
# liebige Anzahl an Argumenten übergeben werden kann, die
# dann einzeln verarbeitet werden.
# Für die Übergabe steht dann eine weitere Erleichterung
# zur Verfügung, bei der ein Asterisks vor den Argumenten
# Python veranlaßt, eine übergebene Menge zunächst in
# einzelne Werte umzuwandeln.
def Funktion(*args):
    Summe = 0
    for x in args:
        Summe += x
    print(Summe)

t = (1, 2, 3, 4, 5)
Funktion(t[0], t[1], t[2], t[3], t[4])

# einfachere Verwendung
Funktion(*t)

# Zu beachten ist, daß sich mit diesen Systematiken eine Reihe
# von Varianten und Kombinationen ergeben, z.B. können hierbei
# auch benannte Parameter eingesetzt werden, wobei dann natürlich
# auf die korrekte Abdeckung geachtet werden muß (vgl. dazu Python3)