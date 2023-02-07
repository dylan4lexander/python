#Tuplas(conjunto ordenado de elementos del mismo tipo que no se puede cambiar)
nombres = ('Alex','Andrea')

print(nombres[0])
print(nombres[1])

#metodo len(nos permite ver cuantos elementos tiene una tupla)
print(len(nombres))

#sabes si un elemento esa en una tupla 
if 'Alex' in nombres:
    print('si')
if 'A' not in nombres:
    print()

#metodos de tuplas
#.count(Este mostrará el número de veces que aparece un elemento en nuestra tupla, como parámetro debemos pasarle el elemento que queremos que cuente)
print(nombres.count('Alex'))
#.index(Este método nos devuelve en que posición se encuentra el elemento que le pasemos como parámetro)
print(nombres.idex('Andrea'))

#iterar en una lista
frutas = ("manzana", "platano", "durazno")
for fruta in frutas:
  print(fruta)