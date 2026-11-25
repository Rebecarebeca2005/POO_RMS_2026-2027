"""Módulo que genera informes de ventas en fichero con with."""


class InformeVentas:
    """Informe de ventas con pie de total o de 'incompleto' si hay error."""

    total_informes = 0
    separador = '-' * 30

    def __init__(self, titulo: str, ruta: str) -> None:
        """Valida y normaliza los datos del informe."""
        if not titulo.strip():
            raise ValueError('El título no puede estar vacío')
        if not ruta.strip():
            raise ValueError('La ruta no puede estar vacía')
        self.titulo = titulo.strip().title()
        self.ruta = ruta.strip()
        self._fichero = None
        self._cerrado = False
        self._total = 0.0
        self._ventas = 0
        InformeVentas.total_informes += 1

    def __enter__(self) -> 'InformeVentas':
        """Abre el fichero y escribe la cabecera."""
        self._fichero = open(self.ruta, 'w', encoding='utf-8')
        self._fichero.write(f'{self.titulo}\n{self.separador}\n')
        return self

    def anadir_venta(self, concepto: str, importe: float) -> None:
        """Escribe una venta y acumula el total."""
        if self._fichero is None or self._fichero.closed:
            raise RuntimeError('El informe no está abierto')
        if not concepto.strip():
            raise ValueError('El concepto no puede estar vacío')
        if importe <= 0:
            raise ValueError('El importe debe ser positivo')
        self._fichero.write(f'{concepto.strip()}: {importe:.2f}\n')
        self._total += importe
        self._ventas += 1

    def total(self) -> float:
        """Total acumulado."""
        return self._total

    def num_ventas(self) -> int:
        """Número de ventas registradas."""
        return self._ventas

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        """Escribe el pie, cierra el fichero y no silencia excepciones."""
        if self._fichero is not None and not self._fichero.closed:
            self._fichero.write(self.separador + '\n')
            if exc_type is None:
                self._fichero.write(f'TOTAL: {self._total:.2f}\n')
            else:
                self._fichero.write(f'INFORME INCOMPLETO: {exc_type.__name__}\n')
            self._fichero.close()
        self._cerrado = True
        return False

    def __del__(self) -> None:
        """Avisa si no se cerró mediante with."""
        try:
            if not self._cerrado:
                print(f'Aviso (__del__): informe {self.ruta} sin cerrar con with')
        except Exception:
            pass


def main() -> None:
    """Demuestra el uso de InformeVentas."""
    i1 = InformeVentas('  ventas de enero ', 'enero.txt')
    i2 = InformeVentas('ventas de febrero', 'febrero.txt')
    print('type:', type(i1), '| isinstance:', isinstance(i1, InformeVentas))
    print('i1:', i1.__dict__)
    print('i2:', i2.__dict__)

    print('Clase:', InformeVentas.separador == i1.separador)
    i1.separador = '=' * 5                         # tapa el de clase solo en i1
    print(i1.separador, '|', i2.separador)
    del i1.separador                               # vuelve a ver el de clase

    with i1:
        i1.anadir_venta('Camisetas', 120.5)
        i1.anadir_venta('Gorras', 30)
    assert i1.total() == 150.5 and i1.num_ventas() == 2
    with open('enero.txt', encoding='utf-8') as f:
        assert f.read() == (
            'Ventas De Enero\n' + '-' * 30 + '\n'
            'Camisetas: 120.50\nGorras: 30.00\n'
            + '-' * 30 + '\nTOTAL: 150.50\n'
        )

    try:
        with i2:
            i2.anadir_venta('Bufandas', 45)
            i2.anadir_venta('Guantes', -3)         # ValueError
    except ValueError as error:
        print('Capturada fuera del with:', error)
    assert i2._fichero.closed
    with open('febrero.txt', encoding='utf-8') as f:
        contenido = f.read()
    assert contenido.endswith('INFORME INCOMPLETO: ValueError\n')
    assert 'Bufandas: 45.00' in contenido

    print('Total informes:', InformeVentas.total_informes)


if __name__ == '__main__':
    main()
