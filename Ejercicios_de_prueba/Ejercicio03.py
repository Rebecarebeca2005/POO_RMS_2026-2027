class Producto: 
    IVA = 0.21  # atributo de clase 
 
    def __init__( 
        self, 
        nombre: str, 
        precio: float, 
        stock: int = 0, 
        codigo: str = "", 
    ) -> None: 
        self.nombre = nombre          # atributo de instancia público 
        self.precio = precio          # atributo de instancia público 
        self._stock = stock           # protegido por convención 
        self.__codigo = codigo        # privado por convención 
 
 
def main() -> None: 
    p1 = Producto("Teclado", 25.0, 10, "T-01") 
    p2 = Producto("Ratón", 15.0, 5, "R-01") 
 
    print("p1.__dict__:", p1.__dict__) 
    print("p2.__dict__:", p2.__dict__) 
 
    print("Producto.IVA:", Producto.IVA) 
    print("p1.IVA:", p1.IVA) 
 
    # Se crea un atributo de instancia que tapa al de clase 
    p1.IVA = 0.10 
    print("Después de p1.IVA = 0.10") 
    print("p1.__dict__:", p1.__dict__) 
    print("Producto.IVA:", Producto.IVA) 
    print("p1.IVA:", p1.IVA) 
    print("p2.IVA:", p2.IVA) 
 
    # Acceso al atributo privado mediante name mangling 
    print("Código privado de p1:", p1._Producto__codigo) 
    p1._Producto__codigo = "T-02" 
    print("p1.__dict__ actualizado:", p1.__dict__) 
 
    # Atributo de clase mutable: ejemplo de problema 
    class Alumno: 
        notas = [] 
 
    a = Alumno() 
    b = Alumno() 
    a.notas.append(7) 
    print("b.notas tras a.notas.append(7):", b.notas) 
 
    class AlumnoCorregido: 
        def __init__(self) -> None: 
            self.notas = [] 
 
    c = AlumnoCorregido() 
    d = AlumnoCorregido() 
    c.notas.append(7) 
    print("d.notas tras c.notas.append(7):", d.notas) 
 
 
if __name__ == "__main__": 
    main() 