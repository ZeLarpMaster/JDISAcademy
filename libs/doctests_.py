class MaClasse:
    def __init__(self, x):
        self.x = x

    def add_one(self):
        """
        Ajoutes 1 à la valeur de x

        >>> objet = MaClasse(10)
        >>> objet == MaClasse(10)
        True
        >>> objet.add_one()
        >>> objet == MaClasse(11)
        True
        >>> objet != MaClasse(10)
        True
        >>> objet == MaClasse(10)  # Montrer une erreur
        True
        """
        self.x += 1

    def __eq__(self, other):
        return self.x == other.x


if __name__ == "__main__":
    import doctest

    # Compatible avec tout framework de test qui se respecte
    doctest.testmod()


# Pour plus d'information: https://docs.python.org/3/library/doctest.html
