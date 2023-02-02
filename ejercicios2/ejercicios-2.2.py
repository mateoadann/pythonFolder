#EJERCICIO N°2

#Creando una función que nos devuelva los numeros primos 
#entre 0 y el argumento que le pasemos.

#crear una función que verifique si un número es primo
def es_primo(num):
    #Verificamos que el número pasa no pueda dividirse por ningún 
    # número entre 2 y ese mismo número -1
    for i in range(2,num-1):
        #Si es dvisible po ralguni retornamos False y termina el bucle
        if num%i==0: return False 
    #Si termina el bucle, significa que no fue divisible entonces es primo
    return True

#Creando función que retorne una lista con todos los primos
def primos_hasta(num):
    #Creamos la lista
    primos = []
    for i in range(3,num+1):
        #Verificamos si el valor es primo
        resultado = es_primo(i)
        #En caso de que lo sea (True) lo agregamos a la lista
        if resultado == True : primos.append(i)
    #Devolvemos la lista
    return primos


resultado = primos_hasta(98)
print(resultado)
        