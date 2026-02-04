from xml import sax

class SchachtDaten(sax.handler.ContentHandler):
    def __init__(self):
        super().__init__()
        self.daten = {}
        self.SchachtNummer = ""
        self.SchachtTiefe = 0
        self.Aktiv = None
        self.Typ = None

    def startElement(self, name, attrs):
        if name == "Objektbezeichnung":
            self.SchachtNummer = ""
            self.Aktiv = "SCHACHTNUMMER"
        elif name == "Schachttiefe":
            self.SchachtTiefe = 0
            self.Aktiv = "SCHACHTTIEFE"

    def endElement(self, name):
        if name == "Objektbezeichnung":
            self.daten[self.SchachtNummer] = 0
        elif name == "Schachttiefe":
            self.daten[self.SchachtNummer] = self.SchachtTiefe
        self.Aktiv = None

    def characters(self, content):
        if self.Aktiv == "SCHACHTNUMMER":
            self.SchachtNummer += content
        elif self.Aktiv == "SCHACHTTIEFE":
            self.SchachtTiefe = content


def lade_dict(dateiname):
    handler = SchachtDaten()
    parser = sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(dateiname)
    return handler.daten

print(lade_dict('SchachtDatenKurz.xml'))