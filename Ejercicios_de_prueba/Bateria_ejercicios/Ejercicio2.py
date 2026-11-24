""""Predice la salida. Ojo: += no hace lo mismo con todos los tipos."""
t = (1, 2)
s = 'hola'
l = [1, 2]
t2, s2, l2 = t, s, l
s2 += ' mundo'
l2 += [3]
t2 += (3,)
print(t, s, l)

"""""s2 += ' mundo' crea una cadena nueva (inmutable): s no cambia.
t2 += (3,) crea una tupla nueva: t no cambia.
l2 += [3] en una lista muta en el sitio (como extend): l y l2 son el mismo objeto, así que l sí cambia."""