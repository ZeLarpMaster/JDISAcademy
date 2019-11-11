import secrets


# Générer un token du genre "70b8b23622a3d234561d97bc10dfb4b9"
print(secrets.token_hex(16))


# Générer un token du genre b"\xab\xf3g\xfc\xf3Xw8\x84L\xa9\xf4)\xe8\x93\xc1"
print(secrets.token_bytes(16))


# Générer un token du genre "oFS5CAuCpEkEkOHkfU1wfQ"
print(secrets.token_urlsafe(16))


# Se protéger des timing attacks
print(secrets.compare_digest("ma cool string", "ma cool string"))  # True


# Pour plus d'information: https://docs.python.org/3/library/secrets.html
