you = {}

name = str(input('Escribe tu nombre\n'))
lastName = str(input('Escribe tu apellido tu apellido\n'))
age = int(input('Escribe tu edad\n'))

you.update({'nombre':name,'apellido':lastName,'edad':age})

for dato, valor in you.items():
  print(f'Tu {dato} es {valor}')