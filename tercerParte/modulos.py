#Modulos propios de python
#Modulos de terceros, los descargas y los usas
#Tus propios módulos

# from modulosSaludar import * #Mala práctica, una de las peores malas prácticas

#import para importar el módulo donde están las funciones que queremos usar
#y 'as' para darle otro nombre en caso que sea necesario
import modulosSaludar as saludarModulo
#También se puede importar SOLO la función que queremos del módulo que le 
# indicamos.
from modulosSaludar import saludar
#En este caso importamos una función del módulo pero cambiandole el nombre
from modulosSaludar import saludo_sin_nombre as sin_nombre

#En la primera variable solo ponemos el nombre de la función porque 
# la importamos de esa manera.
saludo_normal = saludar('Mateo')
#Pero en este caso tuvimos que poner el nombre del módulo seguido del nombre
# de la función porque así lo importamos
saludar_raraso = saludarModulo.saludar_raro('Mateo')
#Y acá usamos el nombre que le pusimos antes para llamar la función
saludo_ortiva = sin_nombre('mateo')




#mostramos los resultados:
print(saludo_normal)
print(saludar_raraso)
print(saludo_ortiva)




