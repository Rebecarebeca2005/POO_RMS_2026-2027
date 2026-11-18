class RegistroTemporal:
    def __init__(self, ruta: str) -> None:
        self.ruta = ruta
        self._fichero = None
        self._cerrado = False

    def __enter__(self):
        self._fichero = open(self.ruta, "a", encoding="utf-8")
        self._fichero.write("Inicio de registro\n")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._fichero is not None and not self._fichero.closed:
            if exc_type is None:
                self._fichero.write("Fin de registro\n")
            else:
                self._fichero.write(f"Error: {exc_type.__name__}\n")
            self._fichero.close()
        self._cerrado = True
        return False

    def escribir(self, texto: str) -> None:
        if self._fichero is None or self._fichero.closed:
            raise RuntimeError("El registro no está abierto")
        self._fichero.write(texto + "\n")

    def __del__(self) -> None:
        try:
            if not self._cerrado:
                print(f"__del__: aviso, recurso {self.ruta} no cerrado con with")
        except Exception:
            pass


def main() -> None:
    with RegistroTemporal("registro.txt") as registro:
        registro.escribir("Operación 1")
        registro.escribir("Operación 2")

    try:
        with RegistroTemporal("registro_error.txt") as registro:
            registro.escribir("Antes del error")
            raise ValueError("Fallo simulado")
    except ValueError as error:
        print("Excepción capturada fuera del with:", error)


if __name__ == "__main__":
    main()