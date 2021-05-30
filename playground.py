def add(*args):
    tot = 0
    for n in args:
        tot += n
    return print(tot)


add(4, 5, 6, 7, 44, 6)


def calculator(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculator(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.make)
