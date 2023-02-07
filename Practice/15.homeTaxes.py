print('Hola, te ayudare a determinar los impuestos que debes pagar por el año anual de la renta de vivienda')
print('Cuanto pagas de renta anualmente?')
renta = float(input())
if renta < 10000:
    print('Pagas el 5 porciento de tu renta a impuestos')
    print(' el 5 porciento es de',(renta*0.05)) 
elif renta >= 10000 and renta <= 20000:
    print('Pagas el 15 porciento de tu renta a impuestos')
    print(' el 15 porciento es de',(renta*0.15)) 
elif renta >= 20001 and renta < 35000:
    print('Pagas el 20 porciento de tu renta a impuestos')
    print(' el 20 porciento es de',(renta*0.20)) 
elif renta >= 35001 and renta <= 60000:
    print('Pagas el 30 porciento de tu renta a impuestos')
    print(' el 30 porciento es de',(renta*0.30)) 
elif renta >= 60001:
    print('Pagas el 45 porciento de tu renta a impuestos')
    print(' el 45 porciento es de',(renta*0.45))
