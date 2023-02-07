materias = ['Matematicas','Español','Ingles','Ciencias sociales','Ciencias naturales']
notas=[]

for i in materias:
  nota= float(input(f'ingresa tu nota en {i} '))
  notas.append(nota)

for i in range(len(materias)):
  print(f'Tu nota en {materias[i]} es {notas[i]}')