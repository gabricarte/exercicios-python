# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
temp = list()
par = list()
impar = list()
newlist = list()
for c in range(0, 7):
    temp.append(int(input('Digite um valor numérico: ')))
for num in temp:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
par.sort()
impar.sort(reverse=True)
newlist.append(par[:])
newlist.append(impar[:])
print(f'Esses são os valores pares e ímpares: {newlist}')
