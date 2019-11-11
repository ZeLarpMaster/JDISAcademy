assert [2, 4, 6] == [a * 2 for a in (1, 2, 3)]

thing = (a * 2 for a in (1, 2, 3))
print(thing)  # <generator object <genexpr> at ...>
assert [2, 4, 6] == list(thing)


def direct():
    return [a * 2 for a in (1, 2, 3)]


def indirect():
    return list((a * 2 for a in (1, 2, 3)))


assert direct() == indirect()


print("Ça fonctionne avec des dictionnaires!")
keys = "a", "b", "c"
expected = {"a": ord("a"), "b": ord("b"), "c": ord("c")}
assert expected == {k: ord(k) for k in keys}


print("Ça fonctionne avec des ensembles!")
assert {"a", "b", "c"} == {k for k in keys}
assert {"a", "b", "c"} == set(keys)


# Pour plus d'information: https://docs.python.org/3.8/tutorial/datastructures.html#list-comprehensions
