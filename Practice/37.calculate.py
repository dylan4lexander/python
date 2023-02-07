nums = int(input('Ingrese los numeros a sumar\n'))
sum = 0 
if nums <= 0:
  print('Ingrese minimo un dato')

for i in range(nums):
    num = float(input("Digite el valor a sumar\n"))
    sum = sum + num
    print(sum)

