#Creando un conjunto con un set()
conjunto = set(['dato1', 'dato2'])

#Metiendo un conjunto dentro de otro conjunto:
conjunto1 = frozenset(['dato1', 'dato2'])
conjunto2 = {conjunto1, 'dato3'}

print(conjunto2)

#TEORÍA DE CONJUNTOS:

conjunto1 = {1, 3, 5, 7}
conjunto2 = {1, 3, 7}

#Verificar si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#Verificar si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 < conjunto1

#Verificar si hay algún número en común:
resultado = conjunto2.isdisjoint(conjunto1)



print(resultado)