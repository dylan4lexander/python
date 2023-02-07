print('Hola, soy py... Hoy te ayudare a saber si un numero es par o impar.')
print('Por favor digita un numero entero')
numero = int(input())

if numero <= 0:
    print('Digite un valor mayor a 0')
elif numero%2==0:
    print('Numero par')
else:
    print('Numero impar')
