#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.#
money = float(input('Quanto você possui em sua carteira?: '))
dolar = money / 3.27
print('O total de dólar que você pode comprar é igual a R$ {}'.format(dolar))
