# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
dic = {}
dic['nome'] = str(input('Digite o nome do aluno: '))
dic['media'] = int(input('Digite a média do aluno: '))
if dic['media'] >= 7:
    dic['situacao'] = 'aprovado'
else:
    dic['situacao'] = 'reprovado'
for k, v in dic.items():
    print(f'{k} é igual a {v}')
