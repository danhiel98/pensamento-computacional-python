objetivo = int(input('Introduzca un número: '))
epsilon = 0.01 # Margen de error
bajo = 0.0 # Número menor a del intervalo a evaluar
alto = max(1.0, objetivo) # Máximo número del intervalo a evaluar
respuesta = (alto + bajo) / 2 # División para empezar a evaluar desde la mitad del intervalo

while abs(respuesta**2 - objetivo) >= epsilon: #Mientras el valor no entre en el margen de error aceptable
    print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}\n')
    if respuesta**2 < objetivo: # Si el valor de la división es menor que el valor buscado, se establece el valor encontrado como mínimo
        bajo = respuesta
    else: # Si el valor encontrado es mayor al buscado, el nuevo máximo es el valor encontrado
        alto = respuesta

    respuesta = (alto + bajo) / 2 # Se vuelve a realizar la división con los nuevos valores mínimos y máximos

print(f'La raiz cuadrada de {objetivo} es {respuesta}')