"""Módulo que modela una cuenta de usuario para una plataforma de formación."""


class CuentaUsuario:
    """Representa una cuenta de usuario con control de acceso e intentos."""

    MAX_INTENTOS = 3
    dominio = "formacion.local"

    def __init__(
        self,
        nombre: str,
        email: str,
        password_hash: str,
        activa: bool = True,
        intentos_fallidos: int = 0,
    ) -> None:
        """Inicializa una nueva instancia de CuentaUsuario."""
        self.nombre = nombre
        self._email = email
        self.__password_hash = password_hash
        self._activa = activa
        self._intentos_fallidos = intentos_fallidos

    def esta_activa(self) -> bool:
        """Indica si la cuenta se encuentra activa."""
        return self._activa

    def puede_iniciar_sesion(self) -> bool:
        """Comprueba si está activa y no ha alcanzado el máximo de intentos."""
        return self._activa and self._intentos_fallidos < self.MAX_INTENTOS

    def perfil_publico(self) -> str:
        """Devuelve una cadena con los datos públicos del usuario."""
        return f"Usuario: {self.nombre} | Dominio: {self.dominio}"

    def consultar_email(self) -> str:
        """Devuelve el correo electrónico protegido del usuario."""
        return self._email

    def activar(self) -> None:
        """Activa la cuenta de usuario."""
        self._activa = True

    def desactivar(self) -> None:
        """Desactiva la cuenta de usuario."""
        self._activa = False

    def cambiar_email(self, nuevo_email: str) -> None:
        """Actualiza el email validando que tenga '@' y el dominio de clase."""
        if "@" not in nuevo_email:
            raise ValueError("El email debe contener '@'.")

        if not nuevo_email.endswith(f"@{self.dominio}"):
            raise ValueError(f"El email debe terminar en @{self.dominio}.")

        self._email = nuevo_email

    def registrar_intento_fallido(self) -> None:
        """Incrementa los fallos y desactiva la cuenta al llegar al límite."""
        self._intentos_fallidos += 1

        if self._intentos_fallidos >= self.MAX_INTENTOS:
            self.desactivar()

    def reiniciar_intentos(self) -> None:
        """Restablece el contador de intentos fallidos a cero."""
        self._intentos_fallidos = 0


def main() -> None:
    """Ejecuta pruebas demostrativas sobre la clase CuentaUsuario."""
    cuenta_uno = CuentaUsuario(
        "Rebeca", "rebeca@formacion.local", "1234", True, 2
    )
    cuenta_dos = CuentaUsuario("Miguel", "miguel@formacion.local", "4321")

    print("Estado inicial cuenta_uno:", cuenta_uno.__dict__)
    print("Estado inicial cuenta_dos:", cuenta_dos.__dict__)

    print("¿Son el mismo objeto?:", cuenta_uno is cuenta_dos)
    print("ID de cuenta_uno:", id(cuenta_uno))
    print("ID de cuenta_dos:", id(cuenta_dos))

    print("Perfil público:", cuenta_uno.perfil_publico())

    cuenta_uno.cambiar_email("rebeca.nueva@formacion.local")
    print("Nuevo email cuenta_uno:", cuenta_uno.consultar_email())

    cuenta_uno.registrar_intento_fallido()
    print("¿Cuenta uno activa tras 3er fallo?:", cuenta_uno.esta_activa())
    print("¿Puede iniciar sesión cuenta_uno?:", cuenta_uno.puede_iniciar_sesion())

    # Comprobación de que modificar cuenta_uno no afecta a cuenta_dos
    print("¿Cuenta dos sigue activa?:", cuenta_dos.esta_activa())
    print("Estado cuenta_dos intacto:", cuenta_dos.__dict__)

    # Prueba de validación con control de excepciones
    try:
        cuenta_dos.cambiar_email("correo_malo@gmail.com")
    except ValueError as error:
        print(f"Error controlado al cambiar email: {error}")

    # Uso de atributo de clase y acceso mediante name mangling
    print("Dominio de la plataforma:", CuentaUsuario.dominio)
    # El name mangling renombra el atributo para evitar colisiones,
    # pero no aporta seguridad real frente a accesos externos.
    print(
        "Hash privado (name mangling):",
        cuenta_uno._CuentaUsuario__password_hash,
    )


if __name__ == "__main__":
    main()