num = int(input('Digite un numero entero positivo\n'))

for i in range(1, num+1):
    if i % 2 == 0:
        continue 
    print(i,end ='-')
