#Escribir
print('Alguna frase bien pensada')
#Concatenacion 
Sujeto = 'Juan'
Predicado = 'Pelea con tiburones'
Frase = Sujeto +' '+ Predicado
print(Sujeto)
print(Predicado)
print(Frase)
#Salto de linea 
print('Arriba \n', 'Abajo')
#Sangria(espaciado)
print ("\t Sangriado")
#Convertir texto a mayusculas(metodo upper)
fraseFilosofica = 'Este... No se. -Valiu'
print(fraseFilosofica.upper())
#Convertir texto a minusculas(metodo lower)
fraseNoFilosofica = 'LA VIDA SOLO TIENE TRES FINALES'
print(fraseNoFilosofica.lower())
#Cambiar solo la primera letra a mayuscula(metodo capitalize)
miNombre = 'dylan'
print(miNombre.capitalize())
#Cambiar mayusculas por minusculas y viceversa(metodo swapcase)
nombre = 'vALIU'
print(nombre.swapcase())
#Convertir texto en titulo(metodo title)
titulo = 'Titleee'
print(titulo.title())
#Parametro end(agregar cualquier cadena de caracteeres al final de la impresion)
Frase = 'No'
print(Frase, end= '- \n')
#Paramwtro sep(nos permite darle formato a la impresion)
print('1','2','3', sep= ', \n')
#Escribir varias lineas
variosFrases = menu = ''' 
1. a
2. b
3. c
'''
print(menu)
#f strings(cuando se usan varias variables en vez de palabras)
x = 1 
y = 2
print(f'{x}, {y}')
#convertir cadenas str y number
var = '23'
int(var)
variabl = True
str(variabl)
print(var, variabl)
#float(convierte a decimal y hace todo mas facil :))(despues doy mejor definicion)
var = 13324329532423
print(float(var))
