# pickle serialisiert beliebige Daten in ein
# proprietäres binäres Format
# zu beachten ist, daß dabei auch Typinforma-
# tionen serialisiert werden

import pickle

# einfachstes Basisbeispiel
with open("D:/Tmp/pickle-test.dat", "wb") as f:
    pickle.dump([1, 2, 3], f)

with open("D:/Tmp/pickle-test.dat", "rb") as f:
    print(pickle.load(f))

MP3 = { }
MP3["Titel"] = "Peaches en Regalia"
MP3["Künstler"] = "Frank Zappa"
MP3["Album"] = "Hot rats"
MP3["Jahr"] = 1969

with open(r"D:\Tmp\PeachesData.bin", "wb") as Ziel:
    pickle.dump(MP3, Ziel)

MP3 = None

with open(r"D:\Tmp\PeachesData.bin", "rb") as Quelle:
    MP3 = pickle.load(Quelle)
    print(MP3["Album"])
