""""Predice la salida y explica por qué:"""
a = [1, 2, 3]
b = a
c = list(a)
b.append(4)
print(a, c)
print(a is b, a is c, a == c)

"""""b = a es un alias: b.append(4) muta la lista que ven a y b. c = list(a) 
es una copia hecha antes del append, así que no cambia. a == c es False porque a ya tiene un 4 más."""