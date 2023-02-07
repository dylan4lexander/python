inaceptable =2400000*0.0
aceptable = 2400000*0.4
meritorio = 2400000*0.6 
print('Ingrese su valoracion')
valoracion = float(input())

if valoracion == 0.0:
    print('Su valoracion es inaceptable')
    print(f'su bonificacion es ', inaceptable)
elif valoracion == 0.4:
    print('Su valoracion es aceptable')
    print(f'su bonificacion es ', aceptable)
elif valoracion >= 0.6:
    print('Su valoracion es meritorio')
    print(f'su bonificacion es ', meritorio)
