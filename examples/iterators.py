class MyIter:
    def __init__(self):
        self.x = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.x += 1
        if self.x >= 10:
            raise StopIteration()
        return self.x


it = iter(MyIter())
print(it)  # <__main__.MyIter object at ...>
assert next(it) == 1
assert next(it) == 2
for x in it:
    print(x, end=" ")  # 3 4 5 6 7 8 9
print()


# Pour plus d'information: https://docs.python.org/3.8/library/stdtypes.html#typeiter
