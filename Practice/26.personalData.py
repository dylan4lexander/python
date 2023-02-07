Andrea = """
nombre = Andrea
edad = 13
fecha de nacimiento = 13-03-2009
color favorito = amarillo
    """
Mateo = """
nombre = Mateo
edad = 25
fecha de nacimiento = 01-20-1998
color favorito = azul
    """
Dylan = """
nombre = Dylan 
edad = 14
fecha de nacimiento = 12-12-2008
color favorito = negro
    """
print('Bienvenido al centro de contactos\n','Ingrese 1 para Andrea\n','Ingrese 2 para Mateo\n','Ingrese 3 para Dylan\n')
usuario = int(input())

match usuario:
    case 1:
        print(Andrea)
    case 2:
        print(Mateo)
    case 3:
        print(Dylan)
