mesesDelAño = {
    1: 'Enero',
    2: 'Febrero',
    3: 'Marzo',
    4: 'Abril',
    5: 'Mayo',
    6: 'Junio',
    7: 'Julio',
    8: 'Agosto',
    9: 'Septiembre',
    10: 'Octubre',
    11: 'Noviembre',
    12: 'Diciembre'
  }

mes = int(input('Digite un numero del 1 al 12\n'))

while mes != 0:
    print(f'El mes equivalente de {mes} es {mesesDelAño[mes]}')
    mes = int(input('Digite un numero del 1 al 12'))
if mes == 0: 
    print('Chao')
if mes != int:
    print('Invalid')


#except keyError:
#    print('No posibles')
