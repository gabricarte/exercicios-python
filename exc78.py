#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. #
lista = []
cont = 0
maior = 0
menor = 0
for c in range(0, 5):
    num = int(input('Digite um valor numérico inteiro: '))
    cont = cont + 1
    lista.append(num)
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < maior:
            menor = num

print(
    f'O maior valor digitado é {maior} que está na {lista.index(maior)+1}ª  posição e o menor é {menor}, que está na  {lista.index(menor)+1}ª posição')
