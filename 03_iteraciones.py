#Tipos de elementos que son iterables

iterCadena = iter('cadena')
iterLista = iter(['l', 'i', 's', 't', 'a'])
iterTupla = iter(('t','u','p','l','a'))
iterConjunto = iter({'c','o','n','j','u','n','t','o'})
iterDiccionario = iter({'d': 1,'i': 2,'c': 3,'c': 4,'i': 5,'o': 6,'n': 7,'a': 8,'r': 9,'i': 10,'o': 11,})

print(iterCadena)
print(iterLista)
print(iterTupla)
print(iterConjunto)
print(iterDiccionario)