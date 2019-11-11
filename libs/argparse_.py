import argparse


parser = argparse.ArgumentParser(description="Mon programme vraiment cool")
parser.add_argument("nombre", type=int, action="store", help="Un entier")
parser.add_argument("--mot", help="Un mot")

# Équivalent d'appeler parse_args() et d'appeler le script avec `python argparse_.py 10 --mot bob`
args = parser.parse_args(["10", "--mot", "bob"])
print("Nombre:", args.nombre)  # 10
print("Mot:", args.mot)  # bob


print("=" * 5, "À vous")  # Faites `python argparse_.py -h` pour voir l'aide générée
args = parser.parse_args()
print("Nombre:", args.nombre)  # Votre nombre
print("Mot:", args.mot)  # Votre mot


# Pour plus d'information: https://docs.python.org/3/library/argparse.html
