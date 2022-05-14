#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.#
produtos = ('borracha', 2,
            'caneta', 3)
print('-'*40)
print(f'{"Listagem de preços":^40}')
print('-'*40)

for posic in range(0, len(produtos)):
    if posic % 2 == 0:
        print(f'{produtos[posic]:.<30}', end=' ')
    else:
        print(f'R$ {produtos[posic]:>7.2f}')
