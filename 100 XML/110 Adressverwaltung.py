from xml.dom import minidom

class Addresses:
    def __init__(self, path):
        self.doc = minidom.parse(path) #1

    def Neu(self, name, email):
        for PersonenKnoten in self.doc.getElementsByTagName("person"): #2
            if PersonenKnoten.getAttribute("name") == name:
                TextKnoten = self.doc.createTextNode(email)  # 3
                ElementKnoten = self.doc.createElement("email")
                ElementKnoten.appendChild(TextKnoten)  # 4
                PersonenKnoten.appendChild(ElementKnoten)
                return

    def Loeschen(self, email):
        EMails = self.doc.getElementsByTagName("email")  # 5
        for Mail in EMails:
            if Mail.firstChild.data == email:
                Person = Mail.parentNode  # 6
                Person.removeChild(Mail)
                Mail.unlink()  # 7

    def Speichern(self, path):
        Datei = open(path, 'w', encoding='utf-8')  # 8
        Datei.write(self.doc.toxml())
        Datei.close()

    def __str__(self):  # 9
        return self.doc.toprettyxml()

if __name__ == "__main__":
    a = Addresses("Adressen.xml")
    a.Loeschen("gz@wer-auch-immer.de")
    a.Neu("Gottlieb Zürn", "Gugelhupf@wer-auch-immer.de")
    a.Speichern("Adressen_1.xml")
    print(a)

# #1: Aus einem XML-Dokument wird ein DOM-Objekt gewonnen
#     und dem Attribut self.doc zugewiesen.
# #2: Die Liste aller person-Elemente wird durchsucht.
# #3: Die neuen Knoten, die eingefügt werden sollen (ein Textknoten
#     und ein Elementknoten) müssen zunächst mittels Methoden aus der
#     Klasse Document erzeugt werden.
# #4: Die neuen Knoten werden als Kinder in die DOM-Struktur eingefügt.
# #5: Eine Liste sämtlicher im Dokument vorkommenden email-Elemente wird
#     erstellt.
# #6: Wenn das Element, das die gesuchte E-Mail-Adresse repräsentiert,
#     gefunden worden ist, braucht man seinen Elternknoten, um es mit der
#     removeChild()-Methode entfernen zu können.
# #7: Das entfernte Element wird mit unlink() von der DOM-Struktur getrennt,
#     um die Garbage Collection zu erleichtern.
# #8: Das XML-Dokument wird als Textdatei unter dem angegebenen Dateinamen
#     gespeichert. Die gelingt auf diese Weise nur, wenn es nur ASCII-Zeichen
#     enthält.
# #9: Durch Überschreiben der magischen Methode __str__() wird ermöglicht,
#     daß in einer einfachen print-Anweisung eine textuelle Darstellung als
#     XML-Dokument ausgegeben wird.