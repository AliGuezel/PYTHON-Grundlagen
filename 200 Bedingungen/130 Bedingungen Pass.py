# In Python ist die Abfolge der Instruktionen durch "Gestaltung"
# geregelt, d.h. u.a. daß einer if-Anweisung mindestens eine
# Zeile mit einer weiteren Anweisung folgen muß, denn eine if-
# Auswertung ohne nachfolgende Anweisung macht keinen Sinn
# ("wenn xy = True mache nichts")
# Was aber, wenn man die nächstfolgende Anweisung erst später
# 'formulieren' möchte.
# Dafür steht das Schlüsselwort pass zur Verfügung, path
# ist gewissermaßen ein Platzhalter, den man später durch
# 'echten Code' ersetzen kann
a = 2
if a > 10:
    pass
else:
    print("!")

# pass kann überall eingesetzt werden, wo eigentlich zwingend
# eine (eingerückte) Instruktion eingefügt werden müßte