# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
while True:
    num = int(input('Digite um valor numérico inteiro [999 para parar] : '))
    if num in lista:
        lista.remove(num)
    else:
        lista.append(num)
    if num == 999:
        lista.remove(999)
        break
lista.sort()
print(lista)
