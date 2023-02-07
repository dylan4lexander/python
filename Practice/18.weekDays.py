print('Digite un numero del 1 al 7')
dia = int(input())
match dia:
    case 1: 
        print('Lunes')
    case 2:
        print('Martes')
    case 3:
        print('Miercoles')
    case 4:
        print('Jueves')
    case 5:
        print('Viernes')
    case 6:
        print('Sabado')
    case 7:
        print('Domingo')
    case _:
        print('Digite un digite correcto')