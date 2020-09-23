def factorial(n):
    """Factorial de un número n
    n int > 0
    returns n!
    """
    print(n)

    if (n == 0):
        return 1
    
    return n * factorial(n-1)

n = int(input('Escribe un entero: '))

print(factorial(n))

import sys
print(sys.getrecursionlimit())