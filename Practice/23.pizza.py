print('¿Que valor tiene la pizza?')
valorDeLaPizza = int(input())
if valorDeLaPizza <= 0:
    print('¿Que valor tiene la pizza?')
    valorDeLaPizza = int(input())

print('¿Que tipo de membresia tiene?\n','1.Ninguna\n','2.Basic\n','3.Medium\n','4.Premiun\n')
tipoDeMembresia = int(input())

match tipoDeMembresia:
    case 1:
        valorAPagar = valorDeLaPizza*0.95
    case 2:
        valorAPagar = valorDeLaPizza*0.90
    case 3:
        valorAPagar = valorDeLaPizza*0.82
    case 4:
        valorAPagar = valorDeLaPizza*0.75
    case _:
        print('Opcion invalida')

print(f'El valor a pagar es de:',valorAPagar)