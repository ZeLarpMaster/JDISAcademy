def mon_generateur():
    yield 1
    yield 1
    yield 2
    yield 3
    yield 5


def autre_generateur():
    yield 0
    yield from mon_generateur()
    yield 8


gen = mon_generateur()
print(gen)  # <generator object mon_generateur at ...>
assert next(gen) == 1
assert next(gen) == 1
for x in gen:
    print(x, end=" ")  # 2 3 5
print()
gen = autre_generateur()
assert next(gen) == 0
for x in gen:  # Vider le générateur
    pass
assert x == 8


def generateur_cool(combien):
    print("Faire des choses importantes")
    value = yield  # Attendre le premier `send`
    for _ in range(combien):
        print(value)
        value = yield value
    print("Valeur finale:", value)
    return "La Fin."


print("Avant la création")
gen = generateur_cool(3)
print("Après la création")
next(gen)  # Initialiser
print("Après l'initialisation")
gen.send(42)  # 42
gen.send(10)  # 10
gen.send("hello")  # hello
try:
    next(gen)  # Valeur finale: None (parce que `next(gen) == gen.send(None)`)
except StopIteration as e:
    print(e.value)  # La Fin.


# Pour plus d'information: https://docs.python.org/3.8/reference/expressions.html#yieldexpr
