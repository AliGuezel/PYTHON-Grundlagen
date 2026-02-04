# wenn man auf close verzichtet, bleibt die Datei
# gesperrt
# Nachfolgender Code in Thonny ausgeführt 
# => man kann Dateiinhalt nicht ändern
#
# aus Visual Studio ist das anders, weil VS
# Sperrungen für Dateien aufhebt

Alben = (
            "Weasels Ripped My Flesh",
            "Chunga’s Revenge",
            "Fillmore East",
            "200 Motels",
            "Just Another Band from L.A.",
            "Waka/Jawaka",
            "The Grand Wazoo",
            "Over-Nite Sensation",
            "Apostrophe",
            "Roxy & Elsewhere",
            "One Size Fits All",
            "Bongo Fury",
            "Zoot Allures",
            "Zappa in New York",
            "Studio Tan",
            "Sleep Dirt",
            "Sheik Yerbouti",
            "Orchestral Favorites",
            "Joe’s Garage, Act I",
            "Joe’s Garage, Act II & III",
       )

Datei = open("D:/tmp/Alben2.txt", "w")
for a in Alben:
    Datei.write("{}\n".format(a))

# eine Möglichkeit, eine Datei 'automatisch zu schließen'
# besteht in der Verwendung von with:
with open("D:/tmp/Alben2.txt", "w") as Datei:
    for a in Alben:
        Datei.write("{}\n".format(a))