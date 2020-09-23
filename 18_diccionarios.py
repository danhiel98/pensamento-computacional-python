diccionario = {
    'Juan': 23,
    'Dinora': 32,
    'Julio': 19
}

print(diccionario.get('Juan'))

diccionario['Juan'] = 37

print(diccionario.get('Juan'))

print('\nLlaves:')
for llave in diccionario.keys():
    print(llave)

print('\nValores:')
for valor in diccionario.values():
    print(valor)

print('\nElementos:')

for llave, valor in diccionario.items():
    print(llave, valor)