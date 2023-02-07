print('Hola... Soy Dodo')
print('Cual es tu nombre?')
nombre = str(input())
print('Un placer conocerte', nombre)
print('El dia de hoy te voy a ayudar a saber si debes o no pagar impuestos, para ello podrias darme ciertos datos')
print('Podrias decirme tu edad?')
edad = int(input())

if edad <= 0:
    print('Escriba una edad correcta')
    print('Podrias decirme tu edad?')
    edad = int(input())

print('podrias decirme cual es tu salario?')
salario = int(input())

if edad>= 18 & salario>= 2500000:
    print('Debes pagar impuestos')
else:
    print('No debes pagar impuestos')
