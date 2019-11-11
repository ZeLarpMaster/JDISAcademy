## Collections

Pour plus d'information: https://docs.python.org/3/library/collections.html


### namedtuple

Sert à créer un tuple, mais dont on peut accéder aux valeurs par clé au lieu des index. `namedtuple` génère une classe par en dessous.

Exemple
```py
Personne = namedtuple("Personne", ("prenom", "nom"))

john = Personne("John", "Doe")
alice = Personne(nom="Bob", prenom="Alice")

print(john)  # Personne(prenom="John", nom="Doe")
print(john[0])  # John
print(john.prenom)  # John
print(alice)  # Personne(prenom="Alice", nom="Bob")
```


### deque

Une double-ended queue comme présenté dans le cours de structure de données. Elle peut être limitée en taille pour faire un tampon rotatif ou non-limitée pour faire des files d'attente normales.


### ChainMap

Pretty much une pile de dictionnaires. Quand on accède à un élément de la ChainMap, ça retourne la valeur du dictionnaire inséré le plus tard qui contient la clé demandée.

Exemple
```py
defaut = {"a": "allo", "b": "bonjour"}
ma_map = ChainMap({"a": "avion"}, defaut)
print(ma_map["a"])  # avion
print(ma_map["b"])  # bonjour

autre_map = ma_map.new_child({"b": "bateau"})
print(autre_map["b"])  # bateau
```


### defaultdict

Un dictionnaire qui appelle une fonction pour obtenir une valeur par défaut lorsqu'on demande une clé qui n'existe pas.

Exemple
```py
dictionnaire = defaultdict(lambda: [])
for k, v in [("a", 1), ("b", 2), ("a", 3)]:
    dictionnaire[k].append(v)
```


### Counter

Un dictionnaire qui sert à compter le nombre d'occurences de certaines valeurs. Le dictionnaire a toujours un nombre comme valeur. Un élément absent du dictionnaire a 0 comme valeur par défaut (comme un `defaultdict(lambda: 0)`)

Exemple
```py
compteur = Counter("aaabbccccd")
print(compteur["a"])  # 3
print(compteur.most_common(3))  # [("c", 4), ("a", 3), ("b", 2)]
```


### OrderedDict

Sert à rien depuis Python 3.7 et CPython 3.6
