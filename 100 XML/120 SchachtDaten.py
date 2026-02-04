from xml.dom import minidom

with open('SchachtDatenKurz.xml') as Datei:
    Daten = minidom.parse(Datei)

Schaechte = Daten.getElementsByTagName('AbwassertechnischeAnlage')
for Schacht in Schaechte:
    BezeichnungsKnoten = Schacht.getElementsByTagName('Objektbezeichnung')[0]
    TiefeKnoten = Schacht.getElementsByTagName('Schachttiefe')[0]
    print(f"{BezeichnungsKnoten.firstChild.nodeValue}:\t{TiefeKnoten.firstChild.nodeValue}")