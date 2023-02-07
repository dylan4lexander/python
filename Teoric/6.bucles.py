#bucles 
#while(mientras)(son bucles que se repetiran siempre que se cumpla una condicion)

a = 1 
b = 2

while a < b:
    print('A<B')
    a = a+1

#break (nos permite hacer que el bucle infinito pare)
while a < b:
    print('A<B')
    if a == 1:
        break

#continue(parecido a break pero no lo para todo, solo nos permite ignorar una parte del codigo y lo demas continuara siendo producido)
while a < b:
    print('A<B')
    if a == 1:
        continue 
    a = 2 

#for(para)(son bucles que se repiten basados en uninicio, final y el avance(como pasa del inicio al final))

for a in range(51):
    print(a)
    a = a+1

