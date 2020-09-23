# Esto no es una tupla
my_tuple = (4)
print(type(my_tuple))

# Tupla de tres valores
my_tuple = (2, 4, 6)
print(type(my_tuple))

other_tuple = ('ocho', 'diez', 'doce')

# Suma de tuplas
my_tuple += other_tuple 
print(my_tuple)

# Desempaquetar tupla y asignar sus valores a variables
x, y, z = other_tuple
print(x, y, z)

def coordenadas():
    return (5, 4)

x, y = coordenadas()

print(f'Coordenadas: ({x},{y})')