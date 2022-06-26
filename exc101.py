def voto(ano):
    idade = 2022 - year
    if idade >= 18:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    elif idade > 16:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        print(f'Com {idade} anos: NÃO VOTA')


# Programa principal
year = int(input('Em que ano você nasceu?: '))
voto(year)
