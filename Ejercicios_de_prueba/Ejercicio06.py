class PerfilUsuario:
    plataforma = "Nexoo"
    max_intentos = 3

    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.__pasword = password
        self.historial_accesos = []

usuario_1 = PerfilUsuario("usuario1", "rebeca@gmail.com", "1234")
usuario_2 = PerfilUsuario("usuario2", "pepito@gmail.com", "5678")

usuario_1.historial_accesos.append("2023-01-01 10:00:00")
usuario_2.historial_accesos.append("2023-01-01 11:00:00")

print("Dict del primer usuario", usuario_1.__dict__)
print("Dict del segundo usuario", usuario_2.__dict__)

print("Password privada del user 1:", usuario_1._PerfilUsuario__pasword)