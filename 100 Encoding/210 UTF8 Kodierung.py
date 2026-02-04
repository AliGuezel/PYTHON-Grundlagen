# Die Codierung aller (Unicode-) Zeichen kann über
# unterschiedliche Verfahren umgesetzt werden, z.B.
# können für alle Zeichen 32 bit eingesetzt werden,
# wie es z.B. beim utf32 der Fall ist

s = "dies ist ein Ströng"
s_bin = s.encode("utf-32")

# es entsteht ein String, der immer 32 bit pro Zeichen
# verwendet, was eine erhebliche Verschwendung dar-
# stellt, weil z.B. ja auch im Deutschen die aller-
# meisten Zeichen im Bereich des ASCII-Zeichensatzes
# liegen
#
# Die Idee ist deshalb, eine dynamische Codierung zu
# verwenden:
# - die ersten 128 Zeichen (ASCII) werden mit 8 bit codiert
# - nachfolgende Zeichen werden mit zwei, drei oder vier
#   Bytes (also 8er Bitblocks) codiert
# Grundlage für 'nachfolgend', also die Reihenfolge ist
# der Codepoint (= Ordinalposition) im Unicode

def CodeAusgabe(Zeichen):
    print(Zeichen)
    print(len(Zeichen))
    print(Zeichen.encode("utf-8"))
    print(list(Zeichen.encode("utf-8")))
    print(len(Zeichen.encode("utf-8")))
    print()

CodeAusgabe("A")
CodeAusgabe("Ä")
CodeAusgabe("🤨")

