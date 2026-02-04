vornamen = ["Hans", "Peter", "Marie"]
nachnamen = ["Meier", "Peterson", "Müller"]
alter = [33,43,12]

zipped = list(zip(vornamen, nachnamen, alter))

for z in zipped:
    print(z)

v, n, a = "Hans, Meier, 33".split(',')