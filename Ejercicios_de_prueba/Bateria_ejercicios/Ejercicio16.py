""""Crea Mascota con nombre, especie y edad. Crea dos instancias, 
muestra sus __dict__ y comprueba con is que son objetos distintos. 
Añade un atributo de clase reino = 'Animalia' y comprueba que ambas lo ven."""

class Mascota:
    reino = "Animalia"
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

m1 = Mascota('Toby', 'perro', 3)
m2 = Mascota('Misi', 'gato', 5)

print(m1.__dict__)
print(m2.__dict__)
print(m1 is m2)
print(m1.reino, m2.reino)