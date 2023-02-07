#Lambda functions(forma resumida de hacer funciones)
mult = lambda num : num * 2 #se ddefine una variable para la funcion y con la palabra clave se declara, al lado va el parametro que recibe y luego lo que hace
result = mult(3) #se le da un valor al parametro
print(result) #se imprime

#Las Lambda Functions pueden recibir múltiples parámetros y operar con ellos.
sum= lambda a,b,c : a + b + c
result = sum(2,3,4)
print(result)

#Lambda function con listas
datosLista = lambda lista : len(lista) #se da la lista como parametro 
lista = [1,2,3,4] 
datos = datosLista(lista)
print(datos)

# Lambda function con tuplas
datosTupla = lambda tupla : len(tupla)
tupla =  (1,2,3,4,5,6,7,8,9,0,1,2,32,32,45,45,32,67,67,54,1,2,3,4,1,2)
print(datosTupla)