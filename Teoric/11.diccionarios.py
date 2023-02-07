#Diccionarios(son una colección de elementos, donde cada uno tiene una llave key y un valor value)

Trabajador1 = {

  "Nombre": "Sara", 
  "Edad": 27, 
  "Documento": 1003882
 
}
print(Trabajador1)

#el método len(nos va a devolver cuantos elementos existen)
print(len(Trabajador1))

#acceder a un valor del diccionario
print(Trabajador1["Nombre"])

#acceder a elementos 
#.get(el método get tiene la misma funcionalidad, acceder al valor de una clave en un diccionario)
print(Trabajador1.get("Edad"))
#.keys(devolverá una tupla con una lista de todas las claves del diccionario)
print(Trabajador1.keys())
#.values(devolverá una tupla con una lista de todos los valores en el diccionario)
print(Trabajador1.values())
#.items(devolverá cada elemento en un diccionario, como tuplas en una lista)
print(Trabajador1.items())

#iterar en un diccionario
for i in Trabajador1:
  print(i)

#Cambiar(para cambiar un valor tenemos que hacer referencia a su llave)
Trabajador1["Edad"] = 20
print(Trabajador1)

#Agregar
Trabajador1["ColorFav"] = "Azul"
print(Trabajador1)

#metodos para eliminar 
#.pop(nos sirve para eliminar el item que nosotros le especifiquemos, para ello debemos pasarle el nombre de la clave el cual queremos eliminar)
Trabajador1.pop("ColorFav")
print(Trabajador1)
#
#.popitem(elimina el último elemento del diccionario)
print(Trabajador1.popitem())
#.clear(vacía todo el diccionario)
Trabajador1.clear()
print(Trabajador1)

#Copiar diccionarios
#.copy()
Trabajador2= Trabajador1.copy()
print(Trabajador2)



