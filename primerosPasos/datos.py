#Definiendo una variable:
nombre = 'Mateo'
print(nombre)

#Definiendo variable con CamelCase
nombreCompleto = 'Mateo'
print(nombreCompleto)

#Definiendo variable con snake_case:
nombre_completo = 'Mateo'
print(nombre_completo)

#concatenar con +
bienvenida = 'Hola ' + 'Como estas?'

#concatenar con f-strings
bienvenida = f'Hola {nombre}  Como estás?'
print(bienvenida)

#Operadores de pertenencia (in / not in)

print('Mateo' in bienvenida)
print('mateo' in bienvenida)


print()
print('------------------------------------------------')
print()

#Tipos de datos compuestos:

#Creando una lista (Se pueden modificar)
lista = ['Mateo Adan', 'Bikepacking', True, 1.72]
print(lista)
print(lista[1])

#Esto es válido
lista[3]= 'Maquinola'

#Creando una tupla (no se puede modificar)
tupla= ('Mateo Adan', 'Bikepacking', True, 1.72)

#Esto NO es válido
#tupla[1]='Cicloturismo'

print(tupla)
print(tupla[1])


#creando un conjunto (set) (no se puede acceder a los elementos por índice
# no almacena datos duplicados)

conjunto= {'Mateo Adan', 'Cicloturismo', True, 1.72}
print(conjunto)
#print(conjunto[3]) -> No se puede acceder al elemento.

#CREANDO UN DICCIONARIO (dict)
diccionario= {
    'nombre' : 'mateo adan',
    'hobby' : 'Bikepacking',
    'edad' : 20
}

print(diccionario['hobby'])

print()
print('------------------------------------------------')
print()

#OPERADORES ARITMÉTICOS:

#Suma y resta ( + y -)
suma = 12 + 10
resta = 12 - 10

#Multiplicación y División ( * y /) 
multiplicacion = 12 * 2
division= 12 / 2 #Devuelve un float

#División Baja // -> Devuelve un entero redondado hacía abajo, deuuelve un int
division_baja = 12 // 5

#Resto o Módulo
resto = 12 % 5

#Pontencia (Exponente) **
potencia = 12**2

print('suma= ' , suma)
print('resta= ' , resta)
print('multiplicacion= ' , multiplicacion)
print('division= ' , division)
print('resto' , resto)
print('division_baja' , division_baja)
print('potencia' , potencia)

print()
print('------------------------------------------------')
print()

#OPERADORES RELACIONALES O DE COMPARACIÓN

#     es igual que    == 
#     es distinto que    != 
#     es menor que    < 
#     es menor o igual que    <= 
#     es mayor que    >
#     es mayor o ogual que    >=

es_igual_que = 5 == 6

es_distinto_de = 5 != 6  
   
menor_que = 5 < 6

mayor_que = 5 > 6

mayor_o_igual = 5 >= 6

menor_o_igual = 5 <= 6


print('5 == 6 =' , es_igual_que)
print('5 != 6 = ' , es_distinto_de)
print('5 < 6 = ', menor_que)
print('5 > 6 = ' , menor_o_igual)
print('5 >= 6 = ' , mayor_que)
print('5 <= 6 = ' , mayor_o_igual)

print()
print('------------------------------------------------')
print()

#CONDICIONALES

#IF-ELSE
edad = 21

if edad >= 18:
    print('podes pasar kpo')
else:
    print('No kpo no podes pasar')

#ELIF

ingreso_mensual = 33

if ingreso_mensual > 10000:
    print('Estás bien económicamente en cualquier parte del mundo')

elif ingreso_mensual > 1000:
    print('estás bien económicamente en latinoamérica')

elif ingreso_mensual > 300:
    print('Podes vivir en Argentina')

else:
    print('Sos pobre en cualquier padre el mundo')
    
    
print()
print('------------------------------------------------')
print()


#OPERADORES LÓGICOS:

# AND
resultado1 = True & True
resultado2 = True & False
resultado3 = False & False
resultado4 = False & True

# OR

resultado5 = True | True
resultado6 = True | False
resultado7 = False | False
resultado8 = False | True

# NOT
resultado9 = not True
resultado10 = not False

print('AND &')
print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)
print()
print('OR |')
print(resultado5)
print(resultado6)
print(resultado7)
print(resultado8)
print()
print('NOT')
print(resultado9)
print(resultado10)

print()
print('------------------------------------------------')
print()



