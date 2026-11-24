""""Crea una clase Cliente que cuente en un atributo de clase cuántos clientes se han creado. 
Comprueba el contador tras crear tres. 
Explica por qué hay que escribir Cliente.total += 1 y no self.total += 1."""

class Cliente:
    total = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Cliente.total += 1

c1, c2, c3 = Cliente('A'), Cliente('B'), Cliente('C')
print(Cliente.total)      # 3