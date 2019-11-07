def func(arg1, *args, arg3, arg4=None, **kwargs):
    print(arg1, args, arg3, arg4, kwargs)


func(1, 2, 3, arg3=4, arg5=5)  # 1 (2, 3) 4 None {"arg5": 5}
func(1, arg3=...)  # 1 () Ellipsis None {}


# Pour plus d'information: https://docs.python.org/3.8/reference/grammar.html
# (ou googlez parce que lire une grammaire c'est un peu lourd; been there done that)
