lista = [1, 2, 3]

lista.append('cuatro')
lista[1] = 'dos'

for item in lista:
    print(item)

a = [2, 4, 6]
b = a # Se asigna la variable por referencia

print(id(a))
print(id(b))

c = [a, b] # Lista que contiene a las listas a y b
print(c)

a.append(8) # Agrega el mismo elemento a las listas `a` y `b` porque acceden al mismo espacio de memoria
print(c)

#Clonación de listas
a = [2, 4, 6]
b = a

# Maneras de clonar listas para que no se asigne la referencia
c = list(a)
d = a[::]
print(id(a))
print(id(b))
print(id(c))
print(id(d))

lista = list(range(100))
print(lista)

print()

doble = [i * 2 for i in lista ]
print(doble)

print()

pares = [i for i in lista if i % 2 == 0]
print(pares)