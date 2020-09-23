objetivo = int(input('Escriba un número: '))
epsilon = 0.01 # Margen de error o precisión
paso = epsilon**2 # Cantidad a aumentar por cada iteración
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon: #Si el margen de error no entró en el margen aceptable
    print(f'No se encontró la raiz cuadrada de {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
