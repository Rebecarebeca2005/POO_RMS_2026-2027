class Libro:
    formato = "papel"  # atributo de clase

    def __init__(self, titulo: str, autor: str, paginas: int = 0) -> None:
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def ficha(self) -> str:
        return f"{self.titulo} ({self.autor}), {self.paginas} páginas"


def main() -> None:
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 471)
    libro2 = Libro("La sombra del viento", "Carlos Ruiz Zafón", 576)

    print("type(Libro):", type(Libro))
    print("type(libro1):", type(libro1))
    print("isinstance(libro1, Libro):", isinstance(libro1, Libro))
    print("libro1 is libro2:", libro1 is libro2)

    print("\n__dict__ de libro1:", libro1.__dict__)
    print("__dict__ de libro2:", libro2.__dict__)

    print("\nAtributo de clase Libro.formato:", Libro.formato)
    print("Atributo de clase visto desde libro1:", libro1.formato)
    print("Atributo de clase visto desde libro2:", libro2.formato)

    libro1.formato = "digital"
    print("\nDespués de libro1.formato = 'digital':")
    print("libro1.formato:", libro1.formato)
    print("libro2.formato:", libro2.formato)
    print("Libro.formato:", Libro.formato)
    print("__dict__ de libro1:", libro1.__dict__)

    print("\nFichas:")
    print(libro1.ficha())
    print(libro2.ficha())


if __name__ == "__main__":
    main()