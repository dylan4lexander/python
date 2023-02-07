#Listas(Son tipos de datos que nos permiten almacenar todos los tipos de datos, son mutables y dinamicas)
nombres = ['Carmen','Alfredo','Marta']

print(nombres[0])
print(nombres[1])
print(nombres[2])

#metodos para las listas
#.append(se puede usar la función append de las listas para agregar un elemento al final de la lista)
nombres.append('Alex')
print(nombres)
#.pop(la función pop, removerá un elemento según el índice que se indique)
nombres.pop(3)
print(nombres)
#.remove(la función remove, removerá un elemento según el valor que este tenga al interior de la lista)
nombres.remove('Carmen')
print(nombres)
#.clear(vacía todos los ítems de una lista)
nombres.clear()
print(nombres)
#.count(cuenta el número de veces que aparece un ítem)
print(nombres.count('Hola'))
#.index(devuelve la posición en el que aparece un ítem (error si no aparece))
nombres = ['Alex']
print(nombres.index('Alex'))
#.reverse(invierte la lista (NO APLICA A CADENAS DE TEXTO))
numeros = [100,50,0]
numeros.reverse()
print(numeros)
#.sort(ordena automáticamente los ítems de una lista por su valor de menor a mayor)
numeros = [100,50,0]
numeros.sort()
print(numeros)

#iterar en una lista
lista = [1,2,3,4,5,6,7,8,9,0]
for numeros in lista:
  print(numeros)
