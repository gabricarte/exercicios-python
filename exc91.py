# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
import random
from time import sleep
from operator import itemgetter
num1 = random.randint(1, 6)
num2 = random.randint(1, 6)
num3 = random.randint(1, 6)
num4 = random.randint(1, 6)
print('Valores sorteados: ')
dic = {}
ranking = []
dic = {'jogador 1': num1, 'jogador 2': num2,
       'jogador 3': num3, 'jogador 4': num4}

for c, v in dic.items():
    print(f' 0 {c} tirou o número {v}')  
    sleep(1)

ranking = sorted(dic.items(), key=itemgetter(1), reverse=True) #Para passar os itens em ordem. 

print('Ranking dos jogadores: ')
for i, v in enumerate(ranking):
    print(f' {i}º lugar:  {v[0]} com {v[1]}.')  
    sleep(1)
