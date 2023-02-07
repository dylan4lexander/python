loteria = []

for i in range(5):
    numero = int(input('Digite un numero de la loteria\n'))
    loteria.append(numero)
    
loteria.sort()
print(loteria)