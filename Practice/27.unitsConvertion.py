print('Bienvenido al conversor de unidades de medida')
print('Digite la cantidad de metros a convertir')
metros = int(input())
print("""
Menu
(Digite el numero de la opcion) 
1.Kilometros
2.Hectometro
3.Decametro
4.Decimetro
5.Centimetro
6.Milimetro
""")
opcion = int(input())

match opcion:
    case 1:
        print('sus metros en kilometros son ',metros*1/1000)
    case 2:
        print('sus metros en hectometros son ',metros*1/100)
    case 3:
        print('sus metros en decametros son ',metros*1/10)
    case 4:
        print('sus metros en decimetros son ',metros*1/0.1)
    case 5:
        print('sus metros en centimetros son ',metros*100/1)
    case 6:
        print('sus metros en milimetros son ',metros*1000/1)
    case _:
        print('Accion invalida')
        