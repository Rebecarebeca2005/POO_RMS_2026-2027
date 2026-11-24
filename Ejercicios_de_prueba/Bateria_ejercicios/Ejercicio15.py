""""Clase Pedido con una lista interna de líneas (producto, precio). 
Modificador agregar_linea(producto, precio) (valida producto no vacío y precio positivo) y consultor total(). 
Comprueba que dos pedidos no comparten líneas."""

class Pedido:
    def __init__(self):
        self._lineas = []

    def agregar_linea(self, producto, precio):      # modificador
        if not producto.strip():
            raise ValueError('Producto vacío')
        if precio <= 0:
            raise ValueError('Precio positivo')
        self._lineas.append((producto.strip(), float(precio)))

    def total(self):                                # consultor
        return sum(precio for _, precio in self._lineas)

p1, p2 = Pedido(), Pedido()
p1.agregar_linea('Teclado', 10)
p1.agregar_linea('Ratón', 5.5)
assert p1.total() == 15.5
assert p2.total() == 0