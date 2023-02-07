print('Hola, soy Dodo... hoy te ayudare a calcular tu IMC')
print('Para calcular tu IMC necesito que me facilites algunos datos')
print('Escribe tu peso')
peso = float(input())
print('Escribe tu altura')
altura = float(input())
imc = float(peso / (altura * altura))

if imc < 18.5: 
    print(f'su imc es ',imc, 'usted es delgado')
elif imc >= 18.6 and imc <= 24.9:
    print(f'su imc es ',imc, 'usted tiene un peso promedio')
elif imc >= 25.0 and imc <= 29.9:
    print(f'su imc es ',imc, 'usted tiene sobrepeso')
elif imc >= 30.0:
    print(f'su imc es ',imc, 'usted tiene obesidad')
