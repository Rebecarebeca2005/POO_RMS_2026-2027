class ProductoAlmacen:
    STOCK_MINIMO_DEFECTO = 5 
    unidad = 'uds'

    def __init__(self, nombre, codigo, stock=0, stock_minimo=None):
        if not nombre.strip():
            raise ValueError("No puede estar vacio")
        if not codigo.strip():
            raise ValueError("No puede estar vacio")
        if stock < 0:
            raise ValueError("No puede estar vacio")
        if stock_minimo is None:
            stock_minimo = self.STOCK_MINIMO_DEFECTO
        if stock_minimo < 0:
            raise ValueError('El stock mínimo no puede ser negativo')

        self.nombre = nombre.strip()
        self.__codigo = codigo.strip().upper()
        self._stock = stock
        self._stock_minimo = stock_minimo
        self._activo = True
        self._movimientos = []

    def consultar_stock(self):
        return self._stock
    
    def necesita_reposicion(self):
        return self._stock <= self._stock_minimo
    
    def historial(self):
        return list(self._movimientos)
    
    def ficha(self):
        return f'{self.nombre} [{self.__codigo}] - {self._stock} {self.unidad}'

    def entrada(self, cantidad):
        if not self._activo:
            raise RuntimeError('Producto inactivo')
        if cantidad <= 0:
            raise ValueError('La cantidad debe ser positiva')
        self._stock = self._stock + cantidad
        self._movimientos.append(('entrada', cantidad))

    def salida(self, cantidad):
        if not self._activo:
            raise RuntimeError('Producto inactivo')
        if cantidad <= 0:
            raise ValueError('La cantidad debe ser positiva')
        if cantidad > self._stock:
            raise ValueError('Stock insuficiente')
        self._stock -= cantidad
        self._movimientos.append(('salida', cantidad))

    def activar(self) -> None:
        """Activa el producto."""
        self._activo = True

    def desactivar(self) -> None:
        """Desactiva el producto."""
        self._activo = False

    def cambiar_stock_minimo(self, minimo: int) -> None:
        if minimo < 0:
           raise ValueError('El stock mínimo no puede ser negativo')
        self._stock_minimo = minimo

"""""main: crea dos productos; muestra __dict__; 
demuestra con is/id() que son distintos; 
comprueba que el historial de uno no afecta al del otro; 
demuestra que modificar la copia devuelta por historial() no cambia el estado interno; 
muestra el atributo de clase y el privado por name mangling; 
provoca errores controlados."""

def main():
    p1 = ProductoAlmacen("Pepo", "t-01", 10)
    p2 = ProductoAlmacen("Ña", "t-02", 0)

    print('p1:', p1.__dict__)
    print('p2:', p2.__dict__)

    print('¿Mismo objeto?', p1 is p2, '| ids distintos:', id(p1) != id(p2))

    p1.entrada(5)
    p1.salida(12)
    assert p1.consultar_stock() == 3
    assert p1.necesita_reposicion()
    assert p2.historial() == []                    # historial propio
    assert p2.consultar_stock() == 0

    copia = p1.historial()
    copia.append(("falso", 99))
    assert len(p1.historial()) == 2

    try:
        p1.salida(100)
    except ValueError as error:
        print("Error controlado", error)
        p1.desactivar()

if __name__ == "__main__":
    main()