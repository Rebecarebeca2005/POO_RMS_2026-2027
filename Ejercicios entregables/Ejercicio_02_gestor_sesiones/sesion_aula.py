"""Módulo para la gestión y registro de sesiones de aula mediante gestores de contexto."""


class SesionAula:
    """Representa una sesión de aula y gestiona su fichero de registro de forma segura.

    Atributos de clase:
        centro (str): Nombre del centro educativo.
        total_sesiones (int): Contador global de instancias creadas.
    """

    centro = "CFGS Python"
    total_sesiones = 0

    def __init__(
        self,
        aula: str,
        profesor: str,
        alumnos: int = 1,
        log_path: str = "registro.txt",
    ) -> None:
        """Inicializa y valida una nueva instancia de SesionAula.

        Argumentos:
            aula: Nombre o identificador del aula.
            profesor: Nombre del docente responsable.
            alumnos: Número de alumnos asistentes (debe ser un entero positivo).
            log_path: Ruta del fichero de texto donde se guardará el registro.

        Raises:
            ValueError: Si algún parámetro de texto está vacío o alumnos no es un
                entero estrictamente positivo.
        """
        if not isinstance(aula, str) or not aula.strip():
            raise ValueError("El aula no puede estar vacía")
        if not isinstance(profesor, str) or not profesor.strip():
            raise ValueError("El profesor no puede estar vacío")
        if not isinstance(alumnos, int) or isinstance(alumnos, bool) or alumnos <= 0:
            raise ValueError("El número de alumnos debe ser un entero positivo")
        if not isinstance(log_path, str) or not log_path.strip():
            raise ValueError("La ruta del archivo de registro no puede estar vacía")

        self.aula = aula.strip().upper()
        self.profesor = profesor.strip().title()
        self.alumnos = alumnos
        self.log_path = log_path.strip()
        self._log = None
        self._cerrada = False

        SesionAula.total_sesiones += 1

    def __enter__(self) -> "SesionAula":
        """Abre el fichero de registro al entrar en el bloque with.

        Returns:
            La propia instancia de SesionAula lista para registrar eventos.
        """
        self._log = open(self.log_path, "a", encoding="utf-8")
        self._log.write(
            f"Inicio de registro: {self.aula} | Profesor: {self.profesor} "
            f"| Alumnos: {self.alumnos}\n"
        )
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        """Cierra el fichero de registro al salir del bloque with, haya o no error.

        Argumentos:
            exc_type: Clase de la excepción si ocurrió alguna, o None.
            exc_value: Instancia de la excepción si ocurrió alguna, o None.
            traceback: Objeto de traza de la excepción, o None.

        Returns:
            False para no silenciar ninguna excepción ocurrida dentro del bloque.
        """
        if self._log is not None and not self._cerrada:
            if exc_type is None:
                self._log.write("Fin de registro de la sesión\n")
            else:
                self._log.write(f"Error en la sesión: {exc_type.__name__}\n")
            self._log.close()
            self._cerrada = True
        return False

    def registrar(self, mensaje: str) -> None:
        """Escribe una línea de actividad en el fichero de registro abierto.

        Args:
            mensaje: Texto descriptivo de la actividad a registrar.

        Raises:
            RuntimeError: Si se intenta escribir cuando el recurso no está abierto
                o ya ha sido cerrado.
        """
        if self._log is None or self._cerrada:
            raise RuntimeError(
                "No se puede registrar en una sesión cerrada o no inicializada"
            )
        self._log.write(mensaje + "\n")

    def __del__(self) -> None:
        """Emite un aviso si la instancia se destruye sin haberse cerrado con with."""
        try:
            if not self._cerrada:
                print(
                    f"Aviso (__del__): la sesión en {self.aula} ({self.log_path}) "
                    "no se cerró mediante un bloque with."
                )
        except Exception:
            pass


def main() -> None:
    """Función principal para demostrar el ciclo de vida y uso de SesionAula."""
    # 1. Crear al menos dos sesiones
    sesion1 = SesionAula("Aula 101", "Laura Gómez", 25, "sesion1.txt")
    sesion2 = SesionAula("Aula 202", "Carlos Ruiz", 18, "sesion2.txt")

    # 2. Mostrar __dict__, type() e isinstance()
    print("--- Inspección de tipos y espacios de nombres ---")
    print("type(SesionAula):", type(SesionAula))
    print("type(sesion1):", type(sesion1))
    print("isinstance(sesion1, SesionAula):", isinstance(sesion1, SesionAula))
    print("__dict__ de sesion1:", sesion1.__dict__)
    print("__dict__ de sesion2:", sesion2.__dict__)

    # 3. Demostrar diferencia entre atributo de clase y de instancia
    print("\n--- Atributo de clase vs de instancia ---")
    print("Centro (clase):", SesionAula.centro)
    print("Centro visto desde sesion1:", sesion1.centro)
    print("Centro visto desde sesion2:", sesion2.centro)

    # Al modificarlo en una instancia, se crea un atributo propio que tapa al de clase
    sesion1.centro = "CFGS Python - Turno Tarde"
    print("Tras modificar sesion1.centro:")
    print("sesion1.centro:", sesion1.centro)
    print("sesion2.centro:", sesion2.centro)
    print("SesionAula.centro:", SesionAula.centro)

    # 4. Usar with correctamente
    print("\n--- Uso normal de with ---")
    with sesion1 as s1:
        s1.registrar("Explicación de gestores de contexto")
        s1.registrar("Ejercicios prácticos realizados")
    print("¿sesion1 cerrada correctamente?:", sesion1._cerrada)

    # 5. Provocar una excepción dentro de un with para comprobar que __exit__ se ejecuta
    print("\n--- Uso de with con excepción ---")
    try:
        with sesion2 as s2:
            s2.registrar("Inicio de práctica en laboratorio")
            raise ValueError("Fallo simulado en el proyector")
    except ValueError as error:
        print("Excepción capturada fuera del with:", error)
    print("¿sesion2 cerrada tras el error?:", sesion2._cerrada)

    # 6. Mostrar el valor de total_sesiones
    print("\n--- Total de sesiones creadas ---")
    print("Total sesiones:", SesionAula.total_sesiones)


if __name__ == "__main__":
    main()