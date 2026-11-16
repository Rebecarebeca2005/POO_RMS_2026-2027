class Producto:
    IVA = 0.21

    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
p = Producto("Teclado", 25.0)
print(p.__dict__)

    