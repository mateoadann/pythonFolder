#Forma no óptima de sumar valores
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados

resultado = suma([3,4,5,2,1,5])
print(resultado)


#Forma ÓPTIMA, utilizando el parámetro args *
def suma_total(numeros):
    return sum([*numeros])

resultado = suma_total([2,3,3,4,6,33,23,45])
print(resultado)


#Lo mismo que arriba pero utilizando el operador * ocmo parámetros (args*)
def suma(nombre, *numbers):
    return f'{nombre}, la suma de tus números es: {sum(numbers)}'

resultado2 = suma('Mateo', 3,2,35,645,23,8)
print(resultado2)


#Orden de los parámetros:
def frase(nombre, apellido, adjetivo):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante = frase('Mateo', 'Adan', 'Kpo')
print(frase_resultante)
frase_resultante2 = frase(apellido='Adan', adjetivo='Kpo', nombre= 'Mateo')
print(frase_resultante2)

#En ambos casos funciona pero siempre y cuando se le agrege a todos los parámetros
#el nombre de la variable.


