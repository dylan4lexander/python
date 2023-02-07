#Map, Filter y Reduce son métodos de las listas que sirven para realizar diferentes funcionalidades, estos son los mas usados y nos devolverá una nueva lista con el resultado del método que hayamos utilizado.
#Map(nos permite hacer un mapeo, lo que hace es aplicar una misma función nos permite aplicar una función sobre los items de un objeto iterable)
num = [1,2,3,4,5]
def multiplicarPorDos(num):
    num = num * 2
    return num
num_2 = list(map(multiplicarPorDos, num))
print(num_2)
#Filter(nos permite filtrar de forma eficiente los elementos usando una función que proporcionamos)
numeros = [1,2,3,4,5,6,7,8,9,10]
numerosPares = list(filter(lambda x : x % 2 == 0, numeros))
print(numerosPares)
#Reduce(paara usar reduce se debe importar)(reduce un iterable a un unico valor)(acepta una funcion y una secuencia y nos devuelve un unico valor)
from functools import reduce
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
