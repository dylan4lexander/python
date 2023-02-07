divisasPosibles = {
  'euro': '€',
  'dolar': '$',
  'yen': '¥'
}

divisa = str(input('Escribe la divisa\n'))
divisa = divisa.lower()
print(f'El simbolo de {divisa} es {divisasPosibles[divisa]} ')