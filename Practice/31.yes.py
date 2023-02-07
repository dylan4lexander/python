print('Diga si para continuar y no para terminar')
respuesta = str(input())
respuesta = respuesta.lower()

while respuesta == 'si':
    print('Diga si para continuar')
    respuesta=str(input())
    respuesta=respuesta.lower()
    
    if respuesta == 'no':
        print('chao')