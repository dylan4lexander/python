#mathCase nos permite estructurar bloques de codigo que se ejecutaran basados en cierta condicion 
#mathcase con numbers
a = 1

match a:
    case 1: 
        print(1)
    case 2:
        print(2)
    case 3:
        print(3)
    case _:
        print(0)
 
#mathcase con strings

b = 'hola'
match b:
    case 'Hola':
        print('Hola')
    case other:
        print('Chao')
