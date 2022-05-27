# O jogo da força é um jogo em que o jogador tem que acertar qual é a palavra proposta, tendo como dica o
# número de letras e o tema ligado à palavra. A cada letra errada, é desenhada uma parte do corpo do enforcado.
print('-'*35)
print('Seja bem-vindo ao jogo da forca!')
print('-'*35)
palavra_secreta = 'banana'
letras_acertadas = ['_', '_', '_', '_', '_', '_']
print(letras_acertadas)
acertou = False
enforcou = False
erros = 0
while not acertou and not enforcou:
    chute = input('Qual a letra?')
    if chute in palavra_secreta:
        posicao = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_acertadas[posicao] = letra
            posicao += 1
    else:
        erros += 1
    acertou = '_' not in letras_acertadas
    enforcou = erros == 6
    print(letras_acertadas)
if acertou:
    print('Você ganhou!!')
else:
    print('Você perdeu!!')
