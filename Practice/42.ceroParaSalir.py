nums = []

num = int(input('Digite un valor(Presione cero para salir)\n'))

while num != 0:
    nums.append(num)
    print(nums)
    num = int(input('Digite un valor(Presione cero para salir)\n'))
else:
    print('Se acabo')