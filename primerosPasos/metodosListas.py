lista = list([1, 534, 23,33,12,987,7,5,6,88])


#devuelve la cantidad de elementos de la lista
resultado = len(lista)

#Agregando un elemento a la lista con append:
lista.append('Caminos de tierras')

#agregando un elemento a la lista en un índice específico.
lista.insert(2, 'La Cumbrecita')

#Agregando varios elementos a la lista
lista.extend(['Cicloturismo', 'Kilometros'])  
#Se agrega una lista a la lista original, por eso se ponen corchetes.

#Eliminando un elemento de la lista por su índice:
lista.pop(0)
lista.pop(-1)  # -1 para eliminiar el último, -2 para el anteúltimo y así con todos

#removiendo un elemento por su valor
#lista.remove("1")

#Eliminando todos los elementos de la lista.
lista.clear()

#Ordena los elementos
lista.sort(reverse=True) #ordena en reversa la lista
lista.sort() #Esto lo ordena de forma ascendente


#invirtiendo los elementos d ela lista.
lista.reverse() #La lista puede estar o no ordenada lo que hace es invertirla

#print(resultado)


#LAS TUPLAS Y LOS CONJUNTOS(SETS) SON INMUTABLES, NO SE LES PUEDE CAMBIAR EL ORDEN
#O LOS ELEMENTOS DE ESTOS.



#Metodos de diccionarios:

diccionario = {
    'nombre' : 'Mateo',
    'apellido' : 'Adan',
    'subs': 600
}

#Nos devuelve un objeto dict_item
clave = diccionario.keys()



#Obteniendo un elemento con get() (si no encuentra nada el programa continua)
valor_de_asdf = diccionario.get('asdf')

#Eliminando todo del diccionario
#diccionario.clear()

#Eliminando un elemento del diccionario
#diccionario.pop("nombre")

#Obteniendo un elemento dict_item iterable.
diccionario_iterable = diccionario.items()


print(diccionario_iterable)



