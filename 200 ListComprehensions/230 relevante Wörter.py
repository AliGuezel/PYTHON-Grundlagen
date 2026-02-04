text = '''
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''

erg = []
Zeilen = text.split('\n')
for Zeile in Zeilen:
    Woerter = Zeile.split()
    for Wort in Woerter:
        if len(Wort) > 3:
            erg.append(Wort)
print(erg)

erg = []
for Zeile in text.split('\n'):
    for Wort in Zeile.split():
        if len(Wort) > 3:
            erg.append(Wort)
print(erg)

w = [[Wort for Wort in line.split() if len(Wort)>3] for line in text.split('\n')]
print(w)
