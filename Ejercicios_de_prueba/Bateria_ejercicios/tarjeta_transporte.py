"""Módulo que modela tarjetas de transporte."""


class TarjetaTransporte:
    """Tarjeta de viaje con saldo, PIN y bloqueo por intentos fallidos."""

    TARIFA = 1.50
    SALDO_MAXIMO = 100.0
    MAX_INTENTOS = 3
    red = 'Red Urbana'

    def __init__(self, titular: str, pin: str, saldo: float = 0.0) -> None:
        """Valida y crea una tarjeta."""
        if not titular.strip():
            raise ValueError('El titular no puede estar vacío')
        if not (isinstance(pin, str) and len(pin) == 4 and pin.isdigit()):
            raise ValueError('El PIN debe tener exactamente 4 dígitos')
        if not 0 <= saldo <= self.SALDO_MAXIMO:
            raise ValueError('Saldo inicial fuera de rango')
        self.titular = titular.strip()
        self._saldo = float(saldo)
        self.__pin = pin
        self._bloqueada = False
        self._intentos_fallidos = 0

    # ---- consultores ----
    def consultar_saldo(self) -> float:
        """Devuelve el saldo actual."""
        return self._saldo

    def esta_bloqueada(self) -> bool:
        """Indica si la tarjeta está bloqueada."""
        return self._bloqueada

    def puede_viajar(self) -> bool:
        """Comprueba que no esté bloqueada y que el saldo cubra la tarifa."""
        return not self._bloqueada and self._saldo >= self.TARIFA

    def resumen_publico(self) -> str:
        """Datos públicos: sin saldo ni PIN."""
        return f'Titular: {self.titular} | Red: {self.red}'

    # ---- modificadores ----
    def recargar(self, cantidad: float) -> None:
        """Añade saldo validando la cantidad y el límite."""
        if cantidad <= 0:
            raise ValueError('La cantidad debe ser positiva')
        if self._saldo + cantidad > self.SALDO_MAXIMO:
            raise ValueError('Se supera el saldo máximo')
        self._saldo += cantidad

    def viajar(self) -> None:
        """Descuenta la tarifa de un viaje."""
        if not self.puede_viajar():
            raise ValueError('Tarjeta bloqueada o saldo insuficiente')
        self._saldo -= self.TARIFA

    def registrar_intento_fallido(self) -> None:
        """Cuenta un fallo y bloquea al llegar al máximo."""
        self._intentos_fallidos += 1
        if self._intentos_fallidos >= self.MAX_INTENTOS:
            self._bloqueada = True

    def desbloquear(self, pin: str) -> None:
        """Desbloquea con el PIN correcto; si no, cuenta un intento fallido."""
        if pin != self.__pin:
            self.registrar_intento_fallido()
            raise ValueError('PIN incorrecto')
        self._bloqueada = False
        self._intentos_fallidos = 0


def main() -> None:
    """Demuestra el uso de TarjetaTransporte."""
    t1 = TarjetaTransporte('Ana', '1234', 10.0)
    t2 = TarjetaTransporte('Luis', '4321')
    print('t1:', t1.__dict__)
    print('t2:', t2.__dict__)
    print('¿Mismo objeto?', t1 is t2, '| ids distintos:', id(t1) != id(t2))

    t1.viajar()
    assert t1.consultar_saldo() == 8.5
    assert t2.consultar_saldo() == 0.0            # t2 no cambia

    try:
        t2.viajar()
    except ValueError as error:
        print('Error controlado:', error)

    t1.recargar(20)
    assert t1.consultar_saldo() == 28.5
    try:
        t1.recargar(500)
    except ValueError as error:
        print('Error controlado:', error)

    for _ in range(3):
        t1.registrar_intento_fallido()
    assert t1.esta_bloqueada() and not t1.puede_viajar()
    assert not t2.esta_bloqueada()
    t1.desbloquear('1234')
    assert t1.puede_viajar()

    print(t1.resumen_publico())
    print('Atributo de clase:', TarjetaTransporte.TARIFA, t1.TARIFA)
    print('PIN por name mangling:', t1._TarjetaTransporte__pin)
    print('Ojo: no es seguridad real, solo evita accesos accidentales.')


if __name__ == '__main__':
    main()
