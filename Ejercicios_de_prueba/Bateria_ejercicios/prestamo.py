"""Módulo que modela préstamos de material de aula con with."""


class Prestamo:
    """Préstamo de material: activo dentro del with, cerrado al salir."""

    total_prestamos = 0
    MAX_DIAS = 7

    def __new__(cls, *args, **kwargs):
        """Crea la instancia (se ejecuta antes que __init__)."""
        print(f'__new__: creando {cls.__name__}')
        return super().__new__(cls)

    def __init__(self, alumno: str, material: str, dias: int = 3) -> None:
        """Valida y normaliza los datos del préstamo."""
        if not alumno.strip():
            raise ValueError('El alumno no puede estar vacío')
        if not material.strip():
            raise ValueError('El material no puede estar vacío')
        if not isinstance(dias, int) or not 1 <= dias <= self.MAX_DIAS:
            raise ValueError(f'Los días deben estar entre 1 y {self.MAX_DIAS}')
        self.alumno = alumno.strip().title()
        self.material = material.strip().lower()
        self._dias = dias
        self._activo = False
        self._cerrado = False
        self._incidencias = []
        Prestamo.total_prestamos += 1
        self.__codigo = f'P{Prestamo.total_prestamos:03d}'

    # ---- gestor de contexto ----
    def __enter__(self) -> 'Prestamo':
        """Activa el préstamo."""
        self._activo = True
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        """Anota el error si lo hubo, desactiva y cierra; no silencia."""
        if exc_type is not None:
            self._incidencias.append(f'Error: {exc_type.__name__}')
        self._activo = False
        self._cerrado = True
        return False

    # ---- consultores ----
    def esta_activo(self) -> bool:
        """Indica si el préstamo está activo."""
        return self._activo

    def dias_prestamo(self) -> int:
        """Días de préstamo actuales."""
        return self._dias

    def incidencias(self) -> list:
        """Copia de las incidencias."""
        return list(self._incidencias)

    def resumen(self) -> str:
        """Resumen con el código privado."""
        return f'{self.__codigo}: {self.material} -> {self.alumno} ({self._dias} días)'

    # ---- modificadores ----
    def anotar_incidencia(self, texto: str) -> None:
        """Anota una incidencia (solo con el préstamo activo)."""
        if not self._activo:
            raise RuntimeError('El préstamo no está activo')
        if not texto.strip():
            raise ValueError('La incidencia no puede estar vacía')
        self._incidencias.append(texto.strip())

    def ampliar(self, dias: int) -> None:
        """Amplía el préstamo sin superar el máximo."""
        if not self._activo:
            raise RuntimeError('El préstamo no está activo')
        if dias <= 0:
            raise ValueError('Los días deben ser positivos')
        if self._dias + dias > self.MAX_DIAS:
            raise ValueError(f'No se puede superar {self.MAX_DIAS} días')
        self._dias += dias

    def __del__(self) -> None:
        """Avisa si no se cerró mediante with."""
        try:
            if not self._cerrado:
                print(f'Aviso (__del__): préstamo de {self.material} sin cerrar con with')
        except Exception:
            pass


def main() -> None:
    """Demuestra el ciclo de vida de Prestamo."""
    p1 = Prestamo('  ana lópez ', 'PORTÁTIL')
    p2 = Prestamo('luis ruiz', 'proyector', 5)
    print('type:', type(p1), '| isinstance:', isinstance(p1, Prestamo))
    print('p1:', p1.__dict__)
    print('p2:', p2.__dict__)
    print('¿Mismo objeto?', p1 is p2, '| ids distintos:', id(p1) != id(p2))

    print('Clase:', Prestamo.MAX_DIAS, '| p1:', p1.MAX_DIAS)
    p1.MAX_DIAS = 30                               # tapa el de clase solo en p1
    print(p1.MAX_DIAS, '|', p2.MAX_DIAS, '|', Prestamo.MAX_DIAS)
    del p1.MAX_DIAS

    with p1:
        assert p1.esta_activo()
        p1.anotar_incidencia('Cargador sin cable')
        p1.ampliar(2)
    assert not p1.esta_activo()
    assert p1.dias_prestamo() == 5
    assert p1.incidencias() == ['Cargador sin cable']
    assert p2.incidencias() == []                  # listas no compartidas

    try:
        with p2:
            p2.ampliar(10)                         # ValueError
    except ValueError as error:
        print('Capturada fuera del with:', error)
    assert p2.incidencias() == ['Error: ValueError']
    assert p2._cerrado

    try:
        p1.anotar_incidencia('Tarde')
    except RuntimeError as error:
        print('Error controlado:', error)

    print(p1.resumen())
    print('Código por name mangling:', p1._Prestamo__codigo)
    print('Total préstamos:', Prestamo.total_prestamos)


if __name__ == '__main__':
    main()
