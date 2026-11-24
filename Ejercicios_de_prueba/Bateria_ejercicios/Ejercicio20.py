class LibroBiblioteca:
    MAX_RENOVACIONES = 2
    biblioteca = "Central"

    def __init__(
        self,
        titulo: str,
        isbn: str,
        codigo_interna: str,
        disponible: bool = True,
        renovaciones: int = 0,
    ) -> None:
        self.titulo = titulo
        self._isbn = isbn
        self.__codigo_interna = codigo_interna
        self._disponible = disponible
        self._renovaciones = renovaciones

    def esta_disponible(self) -> bool:
        return self._disponible

    def puede_renovarse(self) -> bool:
        return not self._disponible and self._renovaciones < self.MAX_RENOVACIONES

    def ficha_publica(self) -> str:
        return f"Título: {self.titulo} | Biblioteca: {self.biblioteca}"

    def consultar_isbn(self) -> str:
        return self._isbn

    def actualizar_isbn(self, nuevo_isbn: str) -> None:
        if len(nuevo_isbn) != 13 or not nuevo_isbn.isdigit():
            raise ValueError("No tiene 13 caracteres o no son dígitos")
        self._isbn = nuevo_isbn

    def prestar(self) -> None:
        if not self._disponible:
            raise ValueError("El libro está ya prestado")
        self._disponible = False
        self._renovaciones = 0

    def renovar(self) -> None:
        if self._disponible:
            raise ValueError("No se puede renovar un libro disponible")
        self._renovaciones += 1
        if self._renovaciones >= self.MAX_RENOVACIONES:
            self.devolver()

    def devolver(self) -> None:
        self._disponible = True
        self._renovaciones = 0


def main() -> None:
    libro1 = LibroBiblioteca("Titulo 1", "1234567890123", "COD-01")
    libro2 = LibroBiblioteca("Titulo 2", "9876543210987", "COD-02")

    assert libro1 is not libro2

    libro1.prestar()
    assert libro1.esta_disponible() is False
    assert libro2.esta_disponible() is True

    libro1.renovar()
    assert libro1.esta_disponible() is False
    libro1.renovar()  # Al llegar a 2 se devuelve solo
    assert libro1.esta_disponible() is True

    print(libro1.__dict__)
    print(libro1._LibroBiblioteca__codigo_interna)


if __name__ == "__main__":
    main()