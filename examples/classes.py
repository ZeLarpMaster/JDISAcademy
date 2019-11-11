class Chose:
    def __init__(self, x):
        self.x = x

    def get_x(self):
        return self.x


chose = Chose(42)
print(type(chose))  # <class '__main__.Chose'>
print(dir(chose))  # [... méthodes spéciales ..., 'get_x', 'x']


AutreChose = type(
    "Chose", (object,), {"get_x": Chose.get_x, "__init__": Chose.__init__}
)
autre_chose = AutreChose(42)

# Ce n'est pas la même classe
assert type(autre_chose) != type(chose)
assert not isinstance(autre_chose, Chose)
assert not isinstance(chose, AutreChose)

# Mais elles ont le même nom
# Parce que le premier argument de type() est le nom de la classe,
# Les deux classes ont exactement le même nom, même si le 2e chose est mis dans la variable AutreChose
assert str(type(autre_chose)) == str(type(chose))

# Et ont les mêmes méthodes
assert dir(autre_chose) == dir(chose)


# Pour plus d'information: https://docs.python.org/3/library/functions.html#type
