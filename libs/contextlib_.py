import contextlib
import io
import sys


class Ressource:
    def __str__(self):
        return "Ressource cool"

    def close(self):
        print("Appel de 'close'")


@contextlib.contextmanager
def ma_ressource(parametre):
    print("2 - Reçu:", parametre)
    print("3 - Obtention de la ressource...")
    try:
        yield Ressource()
    finally:
        print("5 - Relâchement de la ressource")


print("=" * 5, "contextmanager", "=" * 5)
print("1 - Avant d'obtenir la ressource")
with ma_ressource("coucou") as ressource:
    print("4 - J'ai reçu la ressource:", ressource)
print("6 - Après l'avoir relâchée")


print("=" * 5, "closing", "=" * 5)
print("1 - Avant d'obtenir la ressource")
with contextlib.closing(Ressource()):
    print("2 - Avec la ressource!")
print("3 - Après l'avoir relâchée")


print("=" * 5, "suppress", "=" * 5)
with contextlib.suppress(ArithmeticError):
    print("À l'intérieur")
    raise ArithmeticError
    print("On se rend jamais ici")
print("Rien a brisé!")


print("=" * 5, "redirect_stdout", "=" * 5)
sortie = io.StringIO()
with contextlib.redirect_stdout(sortie):
    print("Bonjour")
sortie.seek(0)
print("On a print: `{}`".format(sortie.read()))


print("=" * 5, "plusieurs contextes", "=" * 5)
sortie = io.StringIO()
with contextlib.redirect_stdout(sortie), contextlib.redirect_stderr(sortie):
    print("Print to stdout")
    print("Print to stderr", file=sys.stderr)
sortie.seek(0)
print("On a print: `{}`".format(sortie.read()))

# Pour plus d'information: https://docs.python.org/3/library/contextlib.html
