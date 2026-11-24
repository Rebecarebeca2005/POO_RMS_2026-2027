""""Clase Rectangulo con base y altura, un consultor area() y un modificador escalar(factor) que multiplique ambos lados (el factor debe ser positivo)."""

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):                      # consultor
        return self.base * self.altura

    def escalar(self, factor):           # modificador
        if factor <= 0:
            raise ValueError('El factor debe ser positivo')
        self.base *= factor
        self.altura *= factor

r = Rectangulo(2, 3)
assert r.area() == 6
r.escalar(2)
assert r.area() == 24