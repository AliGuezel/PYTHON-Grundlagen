from xml.dom import minidom

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

# gruppe            Wurzel-Knoten
# bezeichnung       Element-Knoten
# Projekt-Team      Text-Knoten


# Die Knotentypen:
print([e for e in dir(minidom.Node) if 'NODE' in e])


print("\n\nXML-Ausgabe")
GruppeDOM = minidom.parseString(doc)
print(GruppeDOM, type(GruppeDOM))
# print(GruppeDOM.toprettyxml(newl=''))
# for p in dir(GruppeDOM):
#     print(p)


print("\n\nDocument/Wurzelknoten")
GruppeKnoten = GruppeDOM.documentElement
print(GruppeKnoten, type(GruppeKnoten), GruppeKnoten.nodeType == minidom.Node.DOCUMENT_NODE)
print(GruppeKnoten.tagName)

# der Wurzelknoten verfügt über mehrere Kind-Knoten
for Knoten in GruppeKnoten.childNodes:
    print(Knoten)

# zu beachten ist, daß in Python auch die Zeilenumbrüche einen Knoten darstellen
print("\n\nKindknoten mit Zeilenumbruch")
BezeichnungKnoten = GruppeKnoten.firstChild
print(BezeichnungKnoten)

# der Nachfolger des Zeilenumbruches ist der nächste Elemente-Knoten
# da es sich um einen Elemente-Knoten handelt, verfügt das Objekt
# über die Eigenschaft tagName
print("\n\nnächster Kindknoten (Elementknoten)")
BezeichnungKnoten = BezeichnungKnoten.nextSibling
print(BezeichnungKnoten)
print(BezeichnungKnoten.tagName)
print(BezeichnungKnoten.nodeType == minidom.Node.ELEMENT_NODE)
print(BezeichnungKnoten.parentNode)

# der Elementknoten 'Bezeichnung' hat selbst keine weiteren Daten
# aber ein Kind-Element, nämlich den Text-Knoten 'Projekt-Team'
print("\n\nTextknoten")
ProjektKnoten = BezeichnungKnoten.firstChild
print(ProjektKnoten)
print(ProjektKnoten.nodeType == minidom.Node.TEXT_NODE)

# Auswertungsbeispiel:
# es werden alle Elemente mit dem Tag 'email' ermittelt
# die zugehörigen Daten befinden sich in dem ersten Kind-
# Knoten, der eigentliche Wert steht in der Eigenschaft
# nodeValue
MailAdressen = GruppeDOM.getElementsByTagName("email")
for Knoten in MailAdressen:
    print(Knoten, type(Knoten))
    print(Knoten.firstChild.nodeValue, Knoten.firstChild.data)

print("\n\nAttribute")
for Knoten in GruppeKnoten.childNodes:
    if Knoten.nodeType == minidom.Node.ELEMENT_NODE:
        print(Knoten.getAttribute('ID'))

# Zugriff auf Attribute
doc = """<?xml version="1.0" ?>
<gruppe bezeichnung="Team">
    <person name="Anselm Kristlein">
        <email>Anselm@Kristlein.de</email>
        <email>ak@wer-auch-immer.de</email>
    </person>
    <person  name="Gottlieb Zürn">
        <email>gz@wer-auch-immer.de</email>
    </person>
</gruppe>"""

GruppeDOM = minidom.parseString(doc)
for PersonenKnoten in GruppeDOM.getElementsByTagName("person"):  # 2
    print(PersonenKnoten.getAttribute("name"))