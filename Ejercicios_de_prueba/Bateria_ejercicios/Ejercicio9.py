"""Crea Vehiculo con matricula (público), _kilometros (protegido) y __numero_bastidor (privado). 
Muestra cómo accedes a cada uno, enseña el __dict__ y explica el name mangling."""

class Vehiculo:
    def __init__(self, matricula, kilometros, bastidor):
        self.matricula = matricula                  # público
        self._kilometros = kilometros               # protegido (convención)
        self.__numero_bastidor = bastidor           # privado (name mangling)

v = Vehiculo('1234ABC', 50000, 'VF1XYZ')
print(v.matricula)
print(v._kilometros)
print(v._Vehiculo__numero_bastidor)   # nombre "mangled"
print(v.__dict__)

""""Python renombra __numero_bastidor a _Vehiculo__numero_bastidor. Evita accesos accidentales y choques de nombres; no es seguridad real."""