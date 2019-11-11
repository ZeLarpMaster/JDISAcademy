# Duck typing
def test(ma_chose):
    print(ma_chose.fonction())


class Chose1:
    def fonction(self):
        return "Je suis chose 1"


class Chose2:
    def fonction(self):
        return "Je suis chose 2"


chose1, chose2 = Chose1(), Chose2()
test(chose1)  # Je suis chose 1
test(chose2)  # Je suis chose 2


# Dynamic typing
a = Chose1()
a = Chose2()
test(a)  # Je suis chose 2
