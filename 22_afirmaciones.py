def primera_letra(lista_palabras):
    primeras_letras = []

    for palabra in lista_palabras:
        # Si no se cumple la condicion se lanza una excepción con la descipción de la derecha
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'No se permiten valores vacíos'

        primeras_letras.append(palabra)
    
    return primeras_letras

lista_palabras = ['Comida', 'Perro', 'Playa', 4]

print(primera_letra(lista_palabras))