#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.#
import random
al1 = input('Informe o nome do primeiro aluno: ')
al2 = input('Informe o nome do segundo aluno: ')
al3 = input('Informe o nome do terceiro aluno: ')
al4 = input('Informe o nome do quarto aluno: ')
tds = al1, al2, al3, al4
sort = random.choice(tds)
print('Parabéns! O aluno sorteado foi o {}'.format(sort))
