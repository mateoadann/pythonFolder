#        https://aprendeconalf.es/docencia/python/ejercicios


#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética 
operacion_aritmética = (((3+2)/(2*5))**2)
#print(operacion_aritmética)

#------------------------------------------------------------------------------------
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
#Después debe mostrar por pantalla la paga que le corresponde.

def salario_correcto(hrs_trabajadas,coste_hora):
    paga_total = hrs_trabajadas * coste_hora
    return paga_total

#variable = salario_correcto(float(input('Cuantas horas trabajas?... ')),float(input('Cuanto vale tu hora?... ')))
#print(variable)

#------------------------------------------------------------------------------------

#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, 
# y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> 
# es el índice de masa corporal calculado redondeado con dos decimales.

#IMC = Peso (kg) / altura (m) 2

def indice_masa_corporal(peso,altura):
    float(peso)
    float(altura)
    imc = round(peso / altura**2 , 2)
    return f'Tu índice de masa corporal es {imc}'

indice_m_c = indice_masa_corporal(85,1.72)

#print(indice_m_c)


#------------------------------------------------------------------------------------


#Escribir un programa que pida al usuario dos números enteros y 
# muestre por pantalla la <n> entre <m> da un cociente <c> 
# y un resto <r> donde <n> y <m> son los números introducidos por el usuario, 
# y <c> y <r> son el cociente y el resto de la división entera respectivamente.

def division(n,m):
    float(n)
    float(m)
    cociente = n // m
    resto = n % m
    return f'El cociente de esta división es {cociente} y el resto es {resto}'

divition = division(100, 3)
#print(divition)

#------------------------------------------------------------------------------------


#Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión.

def inversion(cant_dinero,interes_anual,cant_años):
    float(cant_dinero)
    int(cant_años)
    inversion_final = cant_dinero*interes_anual*cant_años
    return f'Tu inversión inicial fue de {cant_dinero} con un interés de {interes_anual} por {cant_años} te da como resultado una inversión total de {inversion_final}'
    








