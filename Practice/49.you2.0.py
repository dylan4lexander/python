you = {}

name = str(input('Escribe tu nombre\n'))
lastName = str(input('Escribe tu apellido tu apellido\n'))
age = int(input('Escribe tu edad\n'))

you.update({'Nombre':name})
you.update({'Apellido':lastName})
you.update({'Edad':age})

for i in you:
  print(i ,you[i])