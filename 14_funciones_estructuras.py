def aplicar_operaciones(num):
    operaciones = [abs, float]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))
    
    return resultado

x = aplicar_operaciones(-10)
print(x)