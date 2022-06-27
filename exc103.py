def ficha(name='<desconhecido>', gols=0):
    print(f'O jogador {name} fez o total de {gols} gols no campeonato')


# Programa principal
nome = str(input('Digite o nome do jogador: '))
gol = str(input('Digite o número de gols do jogador no campeonato: '))

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gols=gol)
else:
    ficha(nome, gol)
