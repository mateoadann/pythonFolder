#la función Lambda es como una arrow function en JavaScript
#En una sola linea de código escribimos una función
#Retornan automáticamente sin necesidad de escribir return
#Sirve para armar funciones que sea rápidas y de una sola acción

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

""" #Función Lambda para multiplicar por 2
multiplicar_por_dos = lambda x : x*2
print(multiplicar_por_dos(2))

#Creando una función común que diga si es par o no:
def es_par(num):
    if (num%2 == 0):
        return True

#Usando filter con una función común:
numeros_pares = filter(es_par, numeros) """

#Creando lo mismo que antes pero con Lambda:
numeros_pares = filter(lambda numero : numero%2 == 0, numeros)

print(list(numeros_pares))


