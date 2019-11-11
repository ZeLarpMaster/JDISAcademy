class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(x={x}, y={y})".format(x=self.x, y=self.y)

    def __str__(self):
        return "<Point x={x} y={y}>".format(x=self.x, y=self.y)

    def __lt__(self, other):
        print("Comparaison de si", self, "est plus petit que", other)
        return self.x < other.x

    def __eq__(self, other):
        print("Comparaison d'égalité de", self, "avec", other)
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        print("Obtention du hash de", self)
        return hash((self.x, self.y))

    def __bool__(self):
        print("Bool-ification de", self)
        return self.x != 0 or self.y != 0


p = Point(2, 3)
print("p\t", p)
print("str(p)\t", str(p))
print("repr(p)\t", repr(p))
print("[p]\t", [p])
print("{!r}\t", "{!r}".format(p))
print("{!s}\t", "{!s}".format(p))
print("{}\t", "{}".format(p))
print("bool(p)\t", bool(p))
print("hash(p)\t", hash(p))

o = Point(4, 6)
assert p < o
assert p != o
assert p and True

# Pour plus d'information: https://docs.python.org/3/reference/datamodel.html#special-method-names
