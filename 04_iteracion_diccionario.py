# Ejemplo de como realizar iteraciones sobre diccionarios

estudiantes = {
    'mexico' : 10,
    'colombia' : 15,
    'el_salvador' : 7
}

print('Iteración sobre llaves')
for pais in estudiantes:
    print(pais)


print('\nIteración sobre llaves 2')
for pais in estudiantes.keys():
    print(pais)

print('\nIteración sobre valores')
for num_estudiantes in estudiantes.values():
    print(num_estudiantes)

print('\nIteración sobre claves y valores')
for pais, num_estudiantes in estudiantes.items():
    print(f'{pais}: {num_estudiantes}')