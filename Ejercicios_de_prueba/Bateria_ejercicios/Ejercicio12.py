"""""Clase Termostato con atributos de clase MIN = 5 y MAX = 30, y atributos protegidos _temperatura y _encendido. 
Consultores: consultar_temperatura() y esta_encendido(). 
Modificadores: encender(), apagar(), subir(grados) y bajar(grados), que validen que grados > 0 y que la temperatura final quede entre MIN y MAX."""

class Termostato:
    MIN = 5
    MAX = 30

    def __init__(self, temperatura=20):
        if not self.MIN <= temperatura <= self.MAX:
            raise ValueError('Temperatura fuera de rango')
        self._temperatura = temperatura
        self._encendido = False

    def consultar_temperatura(self):
        return self._temperatura

    def esta_encendido(self):
        return self._encendido

    def encender(self):
        self._encendido = True

    def apagar(self):
        self._encendido = False

    def subir(self, grados):
        if grados <= 0:
            raise ValueError('Los grados deben ser positivos')
        if self._temperatura + grados > self.MAX:
            raise ValueError('Supera la temperatura máxima')
        self._temperatura += grados

    def bajar(self, grados):
        if grados <= 0:
            raise ValueError('Los grados deben ser positivos')
        if self._temperatura - grados < self.MIN:
            raise ValueError('Baja de la temperatura mínima')
        self._temperatura -= grados

t = Termostato()
t.subir(5)
assert t.consultar_temperatura() == 25