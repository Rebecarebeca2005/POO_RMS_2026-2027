class Carrito:
    def __init__(self):
        self.productos = []

    def anadir(self, p):
        self.productos.append(p)

a, b = Carrito(), Carrito()
a.anadir('pan')
assert b.productos == []
