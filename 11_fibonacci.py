def fibonacci(n):
    """Serie fibonacci

    Args:
        n int: Número de iteraciones
    """

    if n == 0 or n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)


numero = int(input('Introduzca un entero: '))
print(fibonacci(numero))
