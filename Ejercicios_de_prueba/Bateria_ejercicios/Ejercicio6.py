"""""Crea una clase Empleado con atributo de clase empresa = 'TechFP' y atributos de instancia nombre y salario. 
Crea dos empleados y muestra sus __dict__. 
Después cambia Empleado.empresa y comprueba qué ven los dos. 
Por último, asigna empresa solo en el primero y vuelve a mostrar todo."""

class Empleado:
    empresa = 'TechFP'

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

e1, e2 = Empleado('Ana', 1800), Empleado('Luis', 2000)
print(e1.__dict__, e2.__dict__)      # sin 'empresa'
Empleado.empresa = 'NuevaEmpresa'
print(e1.empresa, e2.empresa)        # los dos ven NuevaEmpresa
e1.empresa = 'Otra'                  # atributo de instancia: tapa al de clase
print(e1.empresa, e2.empresa, Empleado.empresa)
print(e1.__dict__)                   # ahora incluye 'empresa'