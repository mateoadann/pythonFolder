#Datos

#EJERCICIO N°1

#función para obtener al asistente y al profesor según la edad.
def obtener_compañeros(cantidad_de_compañeros):#Se le pide como parámetro la cantidad de chicos que hay
    
    #Se crea la lista con los compañeros, empieza vacía porque todavía no se cargó ninguno
    compañeros = []
    #Ejecutamos un for para pedir información de cada compañero.
    for i in range(cantidad_de_compañeros):
        nombre = input('Ingrese el nombre del compañero: ')
        edad = int(input('Ingrese la edad del compañero: '))
        compañero = (nombre, edad)
        #Agregando la información a la lista
        compañeros.append(compañero)
    #Ordenamos de menor a mayor según su edad
    compañeros.sort(key=lambda x : x[1])
    #Compañeros[x] devuelve una tupla con (nombre, edad) 
    # y después accedemos al nombre para definir al asistente y al profesor 
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    #Retornamos una tupla
    return asistente, profesor

#Desempaquetamos lo que nos retorna la función
asistente, profesor = obtener_compañeros(5)
#Mostramos el resultado
print(f'El asistente es {asistente}')
print(f'El profesor es {profesor}')























