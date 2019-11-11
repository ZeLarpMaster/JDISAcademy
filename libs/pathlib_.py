from pathlib import Path


cwd = Path(".")
examples = cwd / ".."
print(examples)  # ..


examples_abs = Path.cwd() / ".."
print(examples_abs)  # <chemin absolu qui fini par /libs/..>


fichier = Path("../examples/async.py")
print(fichier)  # ../examples/async.py
print(fichier.stem)  # async
print(fichier.name)  # async.py
print(fichier.suffix)  # .py
print(fichier.suffixes)  # [".py"]
print(fichier.with_suffix(".md"))  # ../examples/async.md
print(fichier.with_name("hinting.py"))  # ../examples/hinting.py
print(fichier.exists())  # True
print(fichier.read_text().splitlines()[0])  # import asyncio


# Pour plus d'information: https://docs.python.org/3/library/pathlib.html
