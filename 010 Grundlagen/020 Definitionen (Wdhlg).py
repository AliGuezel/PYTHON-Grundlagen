# string
s = "Gugelhupf"
for c in s:
    print(c, end="-")
print()
    
# tuple
t = (1, 2, 3, 4, 5)
for z in t:
    print(z, end="-")
print()

# Liste
l = [1, 2, 3, 4, 5]
for z in l:
    print(z, end="-")
print()

# Wörterbuch
w = { 1 : "A", 2 : "B", 3 : "C"}
for c in w.values():
    print(c, end="-")
print()

# Set
s = {1, 2, 3, 4, 5, 4, 3, 2, 1}
for z in s:
    print(z, end="-")
print()

# Frozensets
f = frozenset({1, 2, 3, 4, 5, 4, 3, 2, 1})
for z in f:
    print(z, end="-")
print()