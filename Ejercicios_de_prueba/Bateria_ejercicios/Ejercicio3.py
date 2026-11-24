def f(lista, texto):
    lista.append(1)
    texto += '!'
    lista = [0]
    return lista

x = [9]
y = 'hi'
r = f(x, y)
print(x, y, r)

""""lista.append(1) muta el objeto original (se ve fuera). 
texto += '!' crea otra cadena y solo cambia el nombre local. 
lista = [0] reasigna el nombre local; 
el objeto de fuera no se toca, pero la función devuelve esa lista nueva."""