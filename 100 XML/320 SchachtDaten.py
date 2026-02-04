from xml.etree import ElementTree

Baum = ElementTree.parse('SchachtDatenKurz.xml')
Wurzel = Baum.getroot()

for Schacht in Wurzel.iter('AbwassertechnischeAnlage'):
    SchachtNummer = Schacht.find('Objektbezeichnung').text
    SchachtTiefe = Schacht.find('Knoten/Schacht/Schachttiefe').text
    print(f"{SchachtNummer}:\t{SchachtTiefe}m")


for StartKnoten in Wurzel.findall('./Datenkollektive/Stammdatenkollektiv/AbwassertechnischeAnlage'):
    SchachtNummer = StartKnoten.findall('./Objektbezeichnung')[0].text
    SchachtTiefe = StartKnoten.findall('./Knoten/Schacht/Schachttiefe')[0].text
    print(f"{SchachtNummer}:\t{SchachtTiefe}m")


