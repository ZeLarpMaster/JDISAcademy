from timeit import timeit


pairs = [0, 2, 4, 6, 8] * 100
impairs = [1, 3, 5, 7, 9] * 100
NUM = 10000


# all
def test_all(liste):
    return all(x % 2 == 0 for x in liste)


print("=" * 5, "all", "=" * 5)
print("Pairs (slower):  ", timeit(lambda: test_all(pairs), number=NUM))
print("Impairs (faster):", timeit(lambda: test_all(impairs), number=NUM))


# any
def test_any(liste):
    return any(x % 2 == 0 for x in liste)


print("=" * 5, "any", "=" * 5)
print("Pairs (faster):  ", timeit(lambda: test_any(pairs), number=NUM))
print("Impairs (slower):", timeit(lambda: test_any(impairs), number=NUM))


# dir
print("=" * 5, "dir", "=" * 5)
print(dir([]))  # [... méthodes spéciales ..., "append", "clear", "copy", ...]
print(dir({}))  # [... méthodes spéciales ..., "clear", "copy", "fromkeys", "get", ...]


# enumerate
print("=" * 5, "enumerate", "=" * 5)
liste = ["allo", "bonjour", "coucou"]
for index, element in enumerate(liste):
    print(index, "=", element)  # 0 = allo 1 = bonjour 2 = coucou


for tuple_ in enumerate(liste):
    print(tuple_)  # (0, "allo") (1, "bonjour") (2, "coucou")


# range
print("=" * 5, "range", "=" * 5)
for nombre in range(10, 20, 2):
    print(nombre)  # 10 12 14 16 18


# reversed
print("=" * 5, "reversed", "=" * 5)
for mot in reversed(liste):
    print(mot)  # coucou bonjour allo


for nombre in reversed(range(10, 20, 2)):
    print(nombre)  # 18 16 14 12 10


# zip
print("=" * 5, "zip", "=" * 5)
liste_anglaise = ["hi", "hello", "hey"]
for mot, mot_anglais in zip(liste, liste_anglaise):
    print(mot, "=", mot_anglais)  # allo = hi bonjour = hello coucou = hey


# Arrête dès qu'un des itérables est terminé
for nombre, mot in zip(range(1000000000), liste):
    print(nombre, "=", mot)  # 0 = allo 1 = bonjour 2 = coucou
