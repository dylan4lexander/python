print('Digite la cantidad de dolares que desea cambiar')
dolares = int(input())
print('A que moneda desea cambiar los dolares\n','1.COP\n','2.MXN\n','3.ARS\n')
cambio = int(input())

match cambio:
    case 1: 
        print('su monto en COP es de ', dolares * 4832.72)
    case 2: 
        print('su monto en MXN es de ', dolares * 19.76)
    case 3:
        print('su monto en ARS es de ', dolares * 169.5)
    case _:
        print('Accion invalida')
