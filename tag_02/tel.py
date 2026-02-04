buecher = { 
    9923: "Tom Sawyer", 
    888: "Huck Finn", 
    77: "Die Leiden des j. Wärters" 
    } # insert via init

telefonbuch_rueckwaerts = {
    "091112345" : "Hans Meier"
}

telefonbuch_vorwaerts = {
    "Hans Meier": "091112345"
}

buecher[123] = "Pipi Langstrumpf" #insert
buecher[123] = "Karlson vom Dach" # update

del buecher[77]

buch = buecher[888] # get
print(buch)

print(buecher[123]) # get
print("")
#for b in buecher.values():
#    print(b)

print(buecher.values())

for k,v in buecher.items():
    print(str(k) + ": " + v)