# Creando un función simple
# def saludar():
#     print('hola')

# #Ejecutando la función simple
# saludar()


# Crear una función con parámetros:
def saludar_a_amigx(nombre):
    print(f'Hola {nombre}, Como estás?')


saludar_a_amigx('Mateo')

# Creando una función que nos retorne múltiples valores
def crear_contraseña_random(num):
    chars = 'abcdefghij'
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    return contraseña, num

#Desempaquetando la función...
password, primer_numero = crear_contraseña_random(2)

#Mostrando los resultados obtenidos
print(f'Tu contraseña nueva es {password}')
print(f'El primer número utilizado para crearla fue: {primer_numero}')