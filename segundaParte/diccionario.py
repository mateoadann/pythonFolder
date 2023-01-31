#Creando diccionario con dict()

diccionario = dict(nombre='mateo',apellido='adan')


#Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(['Mateo', 'Facha']): 'ajjajaj'}


#Creado diccionarios con fromkeys(). Itera sobre el primer valor dando le el valor de 'apellido'
diccionario = dict.fromkeys('nombre','apellido')

#Creando diccionario con fromkeys() con valor por defecto 'none'
diccionario = dict.fromkeys(['nombre','apellido'])


#Creando diccionario con fromkeys() cambiando el valor por defecto a 'no se'
diccionario = dict.fromkeys(['nombre','apellido'], 'nose')














print(diccionario)

