"""Módulo para la auditoría de turnos de caja mediante gestores de contexto."""


class AuditoriaCaja:
    """Gestiona el registro seguro de operaciones de una caja bancaria."""

    entidad = "Banco Python"
    total_auditorias = 0

    def __init__(
        self,
        caja: str,
        cajero: str,
        saldo_inicial: int = 100,
        ruta_log: str = "caja.log",
    ) -> None:
        if not isinstance(caja, str) or not caja.strip():
            raise ValueError("El identificador de caja no puede estar vacío")
        if not isinstance(cajero, str) or not cajero.strip():
            raise ValueError("El nombre del cajero no puede estar vacío")
        if (
            not isinstance(saldo_inicial, int)
            or isinstance(saldo_inicial, bool)
            or saldo_inicial < 0
        ):
            raise ValueError("El saldo inicial debe ser un entero mayor o igual a 0")
        if not isinstance(ruta_log, str) or not ruta_log.strip():
            raise ValueError("La ruta del log no puede estar vacía")

        self.caja = caja.strip().upper()
        self.cajero = cajero.strip().title()
        self.saldo_inicial = saldo_inicial
        self.ruta_log = ruta_log.strip()
        self._fichero = None
        self._finalizada = False

        AuditoriaCaja.total_auditorias += 1

    def __enter__(self) -> "AuditoriaCaja":
        self._fichero = open(self.ruta_log, "a", encoding="utf-8")
        self._fichero.write(
            f"APERTURA CAJA: {self.caja} | Cajero: {self.cajero} "
            f"| Saldo: {self.saldo_inicial}\n"
        )
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if self._fichero is not None and not self._finalizada:
            if exc_type is None:
                self._fichero.write("CIERRE DE CAJA CORRECTO\n")
            else:
                self._fichero.write(
                    f"CIERRE DE CAJA POR ERROR: {exc_type.__name__}\n"
                )
            self._fichero.close()
            self._finalizada = True
        return False

    def anotar_operacion(self, concepto: str) -> None:
        if self._fichero is None or self._finalizada:
            raise RuntimeError(
                "No se puede operar en una caja cerrada o no abierta con with"
            )
        self._fichero.write(concepto + "\n")

    def __del__(self) -> None:
        try:
            if not getattr(self, "_finalizada", True):
                print(
                    f"Aviso (__del__): la auditoría de {self.caja} "
                    f"({self.ruta_log}) no se cerró con un bloque with."
                )
        except Exception:
            pass


def main() -> None:
    aud1 = AuditoriaCaja("caja 01", "ana martínez", 500, "caja1.log")
    aud2 = AuditoriaCaja("caja 02", "luis pérez", 300, "caja2.log")

    print("--- Inspección ---")
    print("type(AuditoriaCaja):", type(AuditoriaCaja))
    print("type(aud1):", type(aud1))
    print("isinstance(aud1, AuditoriaCaja):", isinstance(aud1, AuditoriaCaja))
    print("__dict__ aud1:", aud1.__dict__)
    print("__dict__ aud2:", aud2.__dict__)

    print("\n--- Atributo de clase vs instancia ---")
    aud1.entidad = "Banco Python - Sucursal Norte"
    print("aud1.entidad:", aud1.entidad)
    print("aud2.entidad:", aud2.entidad)
    print("AuditoriaCaja.entidad:", AuditoriaCaja.entidad)

    print("\n--- Uso correcto de with ---")
    with aud1 as a1:
        a1.anotar_operacion("Ingreso efectivo: +200 EUR")
        a1.anotar_operacion("Pago recibo: -45 EUR")
    assert aud1._finalizada is True

    print("\n--- Uso de with con excepción ---")
    try:
        with aud2 as a2:
            a2.anotar_operacion("Retirada ventanilla: -100 EUR")
            raise ValueError("Descuadre de efectivo")
    except ValueError as error:
        print("Error capturado:", error)
    assert aud2._finalizada is True

    print("\n--- Instancia sin cerrar (dispara __del__) ---")
    aud3 = AuditoriaCaja("caja 03", "marta soler", 0, "caja3.log")
    del aud3

    print("\nTotal auditorías creadas:", AuditoriaCaja.total_auditorias)


if __name__ == "__main__":
    main()