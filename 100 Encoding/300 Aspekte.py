
# Im Zusammenhang mit Unicode entsteht die Schwierigkeit
# des Vergleichs (Sortierung) bei manchen Zeichen
# das Zeichen ê kann beispielweise mit zwei Varianten dargestellt
# werden
s1 = "\u00EA"
s2 = "\u0065\u0302"
print(s1, len(s1))
print(s2, len(s2))
print(s1 == s2)

# Eine Lösung besteht darin, die Methode normalize
# aus dem Modul unicodedata zu verwenden
import unicodedata

def StringVergleich(st1, st2):
    def NFD(s):
        return unicodedata.normalize('NFD', s)

    return NFD(st1) == NFD(st2)

print(StringVergleich(s1, s2))
