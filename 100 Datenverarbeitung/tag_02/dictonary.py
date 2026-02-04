buecher = {
    9923: "Tom Sawyer", 
    888: "Huck Finn",
    77: "Die Leiden des J. Wärters"
    }

buecher[123] = "Pipi Langstrumpf" #insert
buecher[123] = "Karlson vom Dach" # update

del buecher[77]

buch = buecher[888] #get
print(buch)

print(buecher[123]) #get
print("")

print(buecher.values())

print(k + ": " + v)
