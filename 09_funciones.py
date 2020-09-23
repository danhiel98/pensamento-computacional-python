def enumeracion(objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raíz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'El número {objetivo} no tiene raíz cuadrada')

def aproximacion(objetivo):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontró la raíz cuadrada de {objetivo}')
    else:
        print(f'La raíz cuadrada de {objetivo} es {respuesta}')

def busqueda_binaria(objetivo):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raíz cuadrada de {objetivo} es {respuesta}')

def opciones():
    print('¿Cuál algoritmo desea utilizar?')
    print('1 - Enumeración')
    print('2 - Aproximación')
    print('3 - Búsqueda binaria')
    print('0 - Salir')

while True:
    opciones()
    opcion = int(input('Seleccione: '))
    
    if opcion == 0:
        break

    objetivo = int(input('Introduzca el número objetivo: '))

    if opcion == 1:
        enumeracion(objetivo)
    elif opcion == 2:
        aproximacion(objetivo)
    elif opcion == 3:
        busqueda_binaria(objetivo)
    else:
        print('Opción no válida')
    
    print('===================')

