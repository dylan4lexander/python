print('Inserte su contraseña para guardarla')
contraseña = str(input())
print('Ingrese su contraseña para acceder')
password = str(input())

while contraseña != password:
    print('Ingrese la contraseña correcta')
    password = str(input())
    if contraseña == password:
        break

if contraseña == password:
    print('Acceso concedido')
