frutas = {
  'manzana': 1000,
  'platano': 2000,
  'pera': 3000,
  'piña':4000
}
fruta = str(input('Que quieres comprar\n'))
fruta= fruta.lower()

kilos = float(input(f'Cuantos kilos vas a comprar de {fruta}?\n'))

print(f'El precio de {kilos} sus kilos de {fruta} es de {frutas[fruta]*kilos} pesos\n')

