numeros = (1,2,3,4,5,6,7,8,9,0,1,2,32,32,45,45,32,67,67,54,1,2,3,4,1,2)

numero = int(input('Digite un valor para buscar cuantas veces esta en la tupla\n'))

if numero not in numeros:
    print('No esta en la tupla')
else:
    print(numeros.count(numero))