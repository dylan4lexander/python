print('Hola, soy py. Hoy te ayudare a hacer divisiones...')
print('Por favor digita el dividendo de nuestra division')
dividendo = int(input())
print('Ahora por favor digita el divisor de nuestra division')
divisor = int(input())

if dividendo <= 0:
    print('digita un divisor mayor a cero')
elif divisor <= 0:
    print('digite un divisor mayor a cero')
else: 
    print(f'el resultado de nuestra division es ',(dividendo/divisor))
