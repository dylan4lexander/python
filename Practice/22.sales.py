print('¿Para que tipo de funcion comprara sus boletas? \n','1.2D\n','2.3D\n')
tipoDeBoleta = int(input())


if tipoDeBoleta == 1:
    boletita = 7000
else:
    boletita = 10000

print('¿De que forma desea pagar?\n','1.Efectivo\n','2.Tarjeta debito o credito\n','3.Tarjeta Royal Films\n')
metodoDePago = int(input())
match metodoDePago:
    case 1:
        valorAPagar = boletita*0.90
    case 2:
        valorAPagar = boletita*0.85
    case 3:
        valorAPagar = boletita*0.80
    case _:
        print('Opcion invalida')



print(f'El valor a pagar es de:',valorAPagar)
