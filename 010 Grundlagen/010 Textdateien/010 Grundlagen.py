DateiName = r"D:\Tmp\Test.txt"

# mit write oder writelines können Daten in die Datei
# geschrieben werden (writeline muß ein iterierbares
# Objekt übergeben werden)
# mit open kann ein Dateiobjekt (<- !!!) erstellt werden:
Datei = open(DateiName, "w")
for i in range(5):
    Datei.write("Zeile" + str(i) + "\n")
Datei.close()

# mit print kann ebenfalls in das Dateiobjekt geschrieben werden
Datei = open(DateiName, "w")
print("Dies eine Zeile für die Datei", file=Datei)
Datei.close()

# für das Lesen stehen dann read, readlines und readline
# zur Verfügung. Beim lesenden Zugriff entsteht eine Aus-
# nahme, wenn die Datei nicht existiert
Datei = open(DateiName, "r")
for s in Datei.readlines():
    print(s, end='')
Datei.close()

# Über die Datei kann aber auch ohne weitere
# Methoden iteriert werden
Datei = open(DateiName, "r")
for s in Datei:
    print(s, end = '')
Datei.close()

