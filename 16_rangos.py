# Rango del 1 al 4
rango = range(1, 5)
for num in rango:
    print(num)

print('\n')
# Rango del 0 al 6 con paso 2
rango2 = range(0, 7, 2)
for num in rango2:
    print(num)

rango3 = range(0, 8, 2)

print()
print(f'Igualdad valores de los rangos: {rango2 == rango3}')
print(f'Igualdad de objetos creados: {rango2 is rango3}')

print('\nNúmeros pares:')
for i in range(0, 101, 2):
    print(i)

print('\nNúmeros impares:')
for i in range(1, 100, 2):
    print(i)