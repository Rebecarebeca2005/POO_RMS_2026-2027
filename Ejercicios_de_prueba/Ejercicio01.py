print(type(10))          
print(type("hola"))      
print(type([1, 2]))      
print(type(len))         
print(type(type))        

a = [1,2,3]
b = a
print(a is b)
print(id(a) == id(b))

a.append(a)
print(b)

c = [1,2,3]
print(a == c)
print(a is c)

lista = [1,2]
lista.append(3)
print(lista)

texto = "hola"
texto_mayus = texto.upper()
print(texto)
print(texto_mayus)

a = [1,2]
b = a.append(3)
print(b)

a = [9,9]
print(a)
print(b)

def añadir(lista):
    lista.append(99)

def reasignar(lista):
    lista = [0,0]

mi_lista = [1]
añadir(mi_lista)
print(mi_lista)

reasignar(mi_lista)
print(mi_lista)

