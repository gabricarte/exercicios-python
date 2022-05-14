# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
while True:
    num = int(input('Digite um valor numérico inteiro [999 para parar] : '))
    lista.append(num)
    if num == 999:
        lista.remove(999)
        break
print(f'O total de números digitados foi {len(lista)}')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O número 5 foi adicionado na lista.')
else:
    print('O número 5 não foi adicionado na lista.')
