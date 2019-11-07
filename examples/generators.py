def my_generator():
    yield 1
    yield 1
    yield 2
    yield 3
    yield 5


def other_generator():
    yield 0
    yield from my_generator()
    yield 8


gen = my_generator()
print(gen)  # <generator object my_generator at ...>
assert next(gen) == 1
assert next(gen) == 1
for x in gen:
    print(x, end=" ")  # 2 3 5
print()
gen = other_generator()
assert next(gen) == 0
for x in gen:  # Empty the generator
    pass
assert x == 8


def cool_generator(how_many):
    print("Do important things")
    value = yield  # Wait until first send
    for _ in range(how_many):
        print(value)
        value = yield value
    print("Final value:", value)
    return "The End."


print("Before creation")
gen = cool_generator(3)
print("After creation")
next(gen)  # Initialize
print("After initialize")
gen.send(42)  # 42
gen.send(10)  # 10
gen.send("hello")  # hello
try:
    next(gen)  # Final value: None (parce que `next(gen) == gen.send(None)`)
except StopIteration as e:
    print(e.value)  # The End.


# Pour plus d'information: https://docs.python.org/3.8/reference/expressions.html#yieldexpr
