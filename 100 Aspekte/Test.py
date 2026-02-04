d = {}
d.update({"A": "ABC", "D": "DEF", "G": "GHI",
          "J": "JKL", "M": "MNO", "P": "PQR"})
print(list(d))
print(dict(list(d.items())[2:4]))