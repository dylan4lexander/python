#metodo pass(nos permite decirle al codigo que cierta parte del codigo se programara despues)
a = 1 
if a == 1:
    pass
else: 
    pass 
#metodo find(nos permite buscar algo en un str(1 si se encuentra y -1 si no))
email = input('Digita tu email: ')
if email.find('@')>=1 and email.find('.')>=1:
  print('correcto')
else:
  print('incorrecto')
#metodos is de los STR en python
str = 'string'
strAlfaNumerico = 'a1b2c3d4'
#isalnum(retorna true si los valores so alfanumericos y false para el caso contrario)
print(strAlfaNumerico.isalnum())
#isalpha(retorna true si los valores son unicamente alfabeticos y false para el caso contrario)
print(str.isalpha())
#isdecimal(retorna true si todos los caracteres en string son decimales y false para el caso contrario)
print(strAlfaNumerico.isdecimal())
#isdigit(retorna true si todos los caracteres en string son digitos y false para el caso contrario)
print(str.isdigit())
#isidentifier(retorna true si el string es un identificador y false para el caso contrario)
print(strAlfaNumerico.isidentifier())
#islower(retorna true si todos los caracteres en string están en minúscula y false para el caso contrario)
print(str.islower())
#isnumeric(retorna true si todos los caracteres en string son numéricos y false para el caso contrario)
print(strAlfaNumerico.isnumeric())
#isprintable(retorna true si todos los caracteres en string son imprimibles y false para el caso contrario)
print(str.isprintable())
#isspace(retorna true si todos los caracteres en string tienen espacios en blanco y false para el caso contrario)
print(strAlfaNumerico.isspace())
#istitle(retorna true si la primera letra de cada palabra del string está en mayúscula y false para el caso contrario)
print(str.istitle())
#isupper(retorna true si todos los caracteres en string están en mayúsculas y false para el caso contrario)
print(strAlfaNumerico.isupper())
