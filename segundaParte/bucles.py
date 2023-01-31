#Iterar listas
animales = ['Perro','Gato','Loro','Cocodrilo','Pez']
numeros = [10, 40, 23, 56, 22]


# #Recorriendo la lista "Animales"
# for animal in animales:
#     print(f'Ahora la varriable "animal" es gual a: {animal}')

# #Recorriendo la lista números y cada número lo multiplicamos por 10
# for num in numeros:
#     resultado = num*10
#     print(f'El resultado de {num} * 10 es igual a: {resultado}')


# #Recorriendo dos listas del mismo tamañano al mismo tiempo:
# for numero, animal in zip(numeros, animales):
#     print(f'Numero : {numero}')
#     print(f'Animal : {animal}')

# #utilizando función range()
# for num in range(5,10): #El primero esta incluido, último NO
#     print(num)

# #Forma NO óptima de recorrer una lista con su índice.
# for num in range(len(numeros)):
#     print(numeros[num])

# #Forma óptima de recorrer una lista con su índice.
# for num in enumerate(numeros): 
#     indice = num[0]
#     valor = num[1]
#     print(f'El índice es: {indice} y el valor es: {valor}')


# #Usando el ELSE en un for
# for num in numeros:
#     print(f'Ejecutando el último bucle, valor actual: {num}')
# else:
#     print(f'El bucle terminó...')


#TODO LO ANTERIOR FUNCIONA IGUAL CON TUPLAS...



frutas = ['Banana', 'Mazana', 'Pera', 'Sandia', 'Melón', 'Durazno']
cadena = 'Hola facha'




for fruta in frutas:
    if fruta == 'Sandia':
        print(f'No comemos mas... la {fruta} me va hacer mal')
        break
    print(f'Me estoy comiendo una {fruta}')
else: #El else no se ejecuta si antes hay un break
    print(f'No como mas fruta')


for fruta in frutas:
    if fruta == 'Pera':
        print(f'No, {fruta} no puedo comer')
        continue
    print(f'Me estoy comiendo una {fruta}')

#Iterar una cadena de texto:
for letra in cadena:
    print(letra)


#for en una sola de linea de código (duplicamos los números)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)







