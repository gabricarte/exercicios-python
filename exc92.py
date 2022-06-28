#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
dic1 = dic2 = {}
dic1 = {'nome':str(input('Digite o nome: ')), 'idade':int(input('Digite o ano de nascimento: ')),'ctps':int(input('Carteira de trabalho (0 não tem): '))}


if dic1['ctps'] == 0:
    for k, v in dic1.items():
        dic1['idade'] = 2022 - dic1['idade']
        print(f'{k} tem o valor de {v}')
else:
    dic2 = dic1.copy()
    dic2['contratação'] = int(input('Qual ano você foi contratado?: '))
    dic2['salario'] = float(input('Digite o salário: '))
    dic2['aposentadoria'] = dic2['contratação'] - dic2['idade'] + 35

for k, v in dic2.items():
    dic2['idade'] = 2022 - dic2['idade']
    print(f'{k} tem o valor de {v}')
