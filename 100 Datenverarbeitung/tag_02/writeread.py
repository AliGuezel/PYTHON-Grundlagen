zeilen = ["erste Zeile", "zweite", "dritte"]

# w = write (überschreiben), a = append (anhängen), r = read (lesen)
with open('meineDatei.txt','w') as f:
    for z in zeilen:
        f.write(f'{z}\n')


with open('meineDatei.txt','r') as f:
    for line in f:
        print(line.strip())

