#funciones:

#Algunos de las funciones más fáciles

#print()
#type()


cadena1 = 'Hola cabeza, como estás?'
cadena2 = 'Aprendiendo Python'


resultado = dir(cadena1) #dir es una función, NO un método
resultado = cadena1.upper() #upper() si es un método.
resultado = cadena1.lower()
resultado = cadena1.capitalize() #Convierte la primera letra en mayúscula.

#Buscamos una cadena en otra cadena:
#resultado = cadena1.find("2")

#buscamos una cadena en otra cadena:
#resultado = cadena1.index("2")

#si es numérico devolvermos true sino es false:
resultado = cadena1.isnumeric()


#Si es alfanumético devolvemos true sino false:
resultado= cadena1.isalpha()


#Buscamos una cadean en otra cadena y devuelve la cantidad de veces que coincida.
resultado = cadena1.count('a')

#contamos cuantos caracterés tiene una cadena
resultado = len(cadena1) #len() es una función, NO un método.


#verificamos si una cadena si empieza con otra cadena dada, si es así devuelve true:
resultado = cadena1.startswith('H')


#verificamos si una cadena si termina con otra cadena dada, si es así devuelve true:
resultado = cadena1.endswith('as?')


#reeplaza un pedazo de la cadena dada por otra.
resultado = cadena1.replace('como', 'Cómo')

#separar cadena con la cadena que le pasamos
resultado = cadena1.split("c")

resultado = dir(cadena1) #dir es una función, NO un método

#print(resultado)
#print(type(resultado))




































