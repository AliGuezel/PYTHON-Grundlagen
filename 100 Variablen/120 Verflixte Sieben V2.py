# Durch die Verwendung von Variablen kann der Code
# entsprechend umgebaut (und vereinfacht) werden

Zahl = 1741

print(Zahl % 7)

Rest = Zahl 
LetzteZiffer = Rest % 10
print(LetzteZiffer % 7)

Rest = Rest // 10
LetzteZiffer = Rest % 10
print(LetzteZiffer % 7)

Rest = Rest // 10
LetzteZiffer = Rest % 10
print(LetzteZiffer % 7)
