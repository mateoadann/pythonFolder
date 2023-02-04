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
    
#------------------------------------------------------------------------------------

#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y 
# los hombres con un nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, 
# y muestre por pantalla el grupo que le corresponde.


def serparar_grupos(cant_alumnos):
    grupo_a = []
    grupo_b = []
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(cant_alumnos):
        nombre = input(f'Ingrese su nombre:  ')
        sexo = input(f'Ingrese su sexo (F / M):  ')
        nombre_min = nombre.lower()
        sexo_min = sexo.lower()
        letra =  abecedario.index(nombre_min[0])
        alumno = [nombre,sexo]
        
        if sexo_min == 'f' and letra <= 12 or sexo_min == 'm' and letra >=13:
            grupo_a.append(alumno)
        elif sexo_min == 'f' and letra >= 13 or sexo_min == 'm' and letra <=12:
            grupo_b.append(alumno)     
        else:
            print(f'Algo salió mal...')
            print(alumno)   
    
    return f'El grupo A está formado por: {grupo_a}, \nEl grupo B está formado por: {grupo_b}'


#serparar_grupos(2)


#------------------------------------------------------------------------------------

#Renta	Tipo impositivo
# Menos de 10000€	       |    5%
# Entre 10000€ y 20000€	  |    15%
# Entre 20000€ y 35000€	  |    20%
# Entre 35000€ y 60000€	  |   30%
# Más de 60000€	          |   45%


def tipo_impositivo(renta_anual):
    float(renta_anual)
    if renta_anual < 10000:
        impuesto = renta_anual*0.05
        impuesto_final = renta_anual - impuesto
    elif 10000 < renta_anual < 20000:
        impuesto = renta_anual*0.15
        impuesto_final = renta_anual - impuesto    
    elif 20000 < renta_anual < 35000:
        impuesto = renta_anual*0.20
        impuesto_final = renta_anual - impuesto
    elif 35000 < renta_anual < 60000:
        impuesto = renta_anual*0.30
        impuesto_final = renta_anual - impuesto
    elif renta_anual >= 60000:
        impuesto = renta_anual*0.45
        impuesto_final = renta_anual - impuesto
        
    return f'Tu renta anual es de {renta_anual} \nTu impuesto es de {impuesto}\nTe queda un resto de {impuesto_final}'



#print(tipo_impositivo(60000))

#------------------------------------------------------------------------------------



















