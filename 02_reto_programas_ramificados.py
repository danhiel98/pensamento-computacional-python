nombre1 = input('Introduzca el nombre del primer usuario: ')
edad1 = int(input('Introduzca la edad del primer usuario: '))

nombre2 = input('Introduzca el nombre del segundo usuario: ')
edad2 = int(input('Introduzca la edad del segundo usuario: '))

if edad1 > edad2:
    print(f'La edad de {nombre1} es mayor que la de {nombre2}')
elif edad1 < edad2:
    print(f'La edad de {nombre2} es mayor que la de {nombre1}')
else:
    print(f'La edad de {nombre1} es la misma que la de {nombre2}')