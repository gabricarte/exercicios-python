dic = {}
gols = []
acum = 0
dic = {'nome': str(input('Digite o nome do jogador: '))}
partidas = int(input(f'Quantas partidas {dic["nome"]} jogou? '))

for c in range(0,partidas):
    gols.append(int(input(f'Digite a quantidade de gols na partida {c}: ')))
    dic['gols'] = gols

for g in gols:
    acum = acum + g
    dic['total'] = acum

print(gols)
print(dic)

for k, v in dic.items():
    print(f'O campo {k} tem valor {v}')
