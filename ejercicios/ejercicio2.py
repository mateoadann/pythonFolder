#Le pedimos al usario que no ingrese una frase
frase = input('Decime una frase y te calculo cuanto tardarías si tuvieras que decirla: ')

#Separamos todas las palabras
palabras_separadas = frase.split(' ')

#Calculamos la cantidad de las palabras
cantidad_de_palabras = len(palabras_separadas)

#En el caso de que tarde mas de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras > 120:
    print(f'Para maestro te fuiste al pasto, no quería un testamento, era una frase...')

print()
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarías {cantidad_de_palabras/2} segundos en decirlo.')
print()
print(f'Dalto lo diría en {cantidad_de_palabras * 100 // 2 * 1.3 / 100} segundos.')

