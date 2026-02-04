# https://docs.python.org/3/library/xml.etree.elementtree.html#xpath-support
from xml.etree import ElementTree

doc = """<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank updated="yes">5</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
</data>"""

Wurzel = ElementTree.fromstring(doc)

# Top-level elements
print(Wurzel.findall("."))

# All 'neighbor' grand-children of 'country' children of the top-level
# elements
for Knoten in Wurzel.findall("./country/neighbor"):
    print(Knoten.attrib)

# Nodes with name='Singapore' that have a 'year' child
for Knoten in Wurzel.findall(".//year/..[@name='Singapore']"):
        print(Knoten.attrib)

# 'year' nodes that are children of nodes with name='Singapore'
for Knoten in Wurzel.findall(".//*[@name='Singapore']/year"):
    print(Knoten.text)

# All 'neighbor' nodes that are the second child of their parent
for Knoten in Wurzel.findall(".//neighbor[2]"):
    print(Knoten.attrib)