def test(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)


arguments = ["a", "b", "c"]
test(*arguments)  # Args: ("a", "b", "c") Kwargs: {}

arguments = {"a": "allo", "b": "bonjour"}
test(**arguments)  # Args: () Kwargs: {"a": "allo", "b": "bonjour"}

arguments = [0, "allo", []]
test("premier", *arguments)  # Args: ("premier", 0, "allo", []) Kwargs: {}

arguments = {"b": "bonjour"}
test(a="allo", **arguments)  # Args: () Kwargs: {"a": "allo", "b": "bonjour"}

# Args: (0, 4, 2, 42) Kwargs: {"x": "chose", "allo": "bonjour"}
test(0, *[4, 2, 42], x="chose", **{"allo": "bonjour"})


# Aussi utilisé dans l'assignation:
qqchose = ("allo", "bonjour")
(allo, bonjour) = qqchose
assert allo == "allo"
assert bonjour == "bonjour"

# On peut omettre les parenthèses
qqchose = "allo", "bonjour"
allo, bonjour = qqchose
assert allo == "allo"
assert bonjour == "bonjour"

# Ou en une seule ligne
allo, bonjour = "allo", "bonjour"
assert allo == "allo"
assert bonjour == "bonjour"

# On peut aussi mettre le surplus à unpack dans une variable
a, *b, e = "a", "b", "c", "d", "e"
assert a == "a"
assert b == ["b", "c", "d"]
assert e == "e"
