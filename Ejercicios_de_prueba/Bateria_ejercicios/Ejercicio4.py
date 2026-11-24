import math


def comprobar():
    def funcion():
        pass

    class Clase:
        pass

    for objeto in (10, 'hola', [1], funcion, Clase, math):
        print(type(objeto), id(objeto))

comprobar()