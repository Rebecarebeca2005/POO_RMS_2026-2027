class Coche:
    ruedas = 4
    def __init__(self, marca):
        self.marca = marca

c1, c2 = Coche('A'), Coche('B')
c1.ruedas = 6
Coche.ruedas = 3
print(c1.ruedas, c2.ruedas, Coche.ruedas)
print(c1.__dict__)