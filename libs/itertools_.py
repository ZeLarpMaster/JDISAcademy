import itertools


liste = ["a", "b"]


print("Permutations:", end=" ")
for a, b in itertools.permutations(liste):
    print(a, b, sep="", end=" ")  # ab ba
print()


print("Produit:", end=" ")
for a, b in itertools.product(liste, liste):
    print(a, b, sep="", end=" ")  # aa ab ba bb
print()


print("Chain:", end=" ")
for x in itertools.chain(["a", "b"], ["c", "d"]):
    print(x, end=" ")  # a b c d
print()


# Pour plus d'information: https://docs.python.org/3/library/itertools.html
