#las funciones son microprocesos reutilizabes en nuestro codigo s
#funciones
def myFirstFunction() :
    print('Primer funcion')

myFirstFunction()
myFirstFunction()
myFirstFunction()
myFirstFunction()
myFirstFunction()

#funciones con parametros
def Function(name):
    print('Hola',name)

Function('A')

#return(da el valor final de la funcion(valor de retorno de la funcion))


def Suma(n1,n2):
    return n1+n2

def Resta(n1,n2):
    return n1-n2

print(Suma(2,4))
print(Resta(2,4))