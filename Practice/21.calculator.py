print('Digite  el primer valor')
n1 = int(input())
print('Digite  el segundo valor')
n2 = int(input())
print('Que desea hacer ? \n','1.Sumar \n','2.Restar \n','3.Multiplicar \n','4.Division')
operacion = int(input())

match operacion:
    case 1: 
        print(n1+n2)
    case 2:
        print(n1-n2)
    case 3:
        print(n1*n2)
    case 4: 
        print(n1/n2)
    case _:
        print('Accion invalida')