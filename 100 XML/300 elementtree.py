from xml.etree import ElementTree

doc = """<?xml version="1.0" ?>
<gruppe>
    <bezeichnung>Projekt-Team</bezeichnung>
    <person ID="A">
        <name>Anselm Kristlein</name>
        <email>Anselm@Kristlein.de</email>
        <email>ak@wer-auch-immer.de</email>
    </person>
    <person ID="B">
        <name>Gottlieb Zürn</name>
        <email>gz@wer-auch-immer.de</email>
    </person>
</gruppe>"""

# Beim Parsing wird zunächst die Datei eingelesen und in einem
# zweiten Schritt muß daraus der Wurzelknoten gewonnen werden
Baum = ElementTree.parse('Adressen.xml')
Wurzel = Baum.getroot()
print(Wurzel)

# Bei einem String werden die Daten sofort in einen Knoten um-
# gewandelt
Wurzel = ElementTree.fromstring(doc)
print(Wurzel)

print(Wurzel.tag)
print(Wurzel.attrib)

for KindKnoten in Wurzel:
    print(KindKnoten.tag, KindKnoten.attrib)

print("\n\nmit find")
print(Wurzel.find('email'))

print("\n\nmit findall")
for Knoten in Wurzel.findall('email'):
    print(Knoten.text)

# iter sucht rekursiv, d.h. alle untergeordneten Knoten werden ermittelt
print("\n\nmit iter")
for Knoten in Wurzel.iter('email'):
    print(Knoten.text)

# XPath-Support
for Knoten in Wurzel.findall('./person/email'):
    print(Knoten.text)