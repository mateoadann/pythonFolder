#Duración de cursos
curso_min = 2.5
curso_max = 7
curso_promedio = 4
curso_dalto = 1.5

#Duración de crudos:
crudo_promedio = 5
crudo_dalto = 3.5

#Diferencias de duraciones:
diferencia_curso_min = 100 - curso_dalto / curso_min * 100
diferencia_curso_max = 100 - curso_dalto * 1000 // curso_max / 10
diferencia_curso_prom = 100 - curso_dalto / curso_promedio * 100

#Calculando el tiempo vacío removido:
tiempo_vacio_primedio = 100 - curso_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - curso_dalto * 1000 // crudo_dalto / 10


#Mostrando la diferencia de duración (ejercicio A)
print(f'El curso de Dalto dura un {diferencia_curso_min}% menos que el curso más rápido ')
print()
print(f'El curso de Dalto dura un {diferencia_curso_max}% menos que el curso mas largo ')
print()
print(f'El curso de Dalto dura un {diferencia_curso_prom}% menos que el curso promedio')

#Mostrando la cantidad de espacios vacios que se remueven (ejercicio B)
print()
print(f'Un curso promedio elimina un  {tiempo_vacio_primedio}% de contenido vacio')
print()
print(f'El curso de Dalto elimina un  {tiempo_vacio_dalto}% de contenido vacio')
print()

#Mostrando diferencias si los cursos duraran 10horas
print(f'Ver 10 horas de este curso equivale a ver {curso_promedio * 100 // curso_dalto / 10} horas de otros cursos')
print('------------')
print(f'Ver 10 horas de otros cursos equivale a ver {curso_dalto * 100 // curso_promedio / 10} horas de este curso')






