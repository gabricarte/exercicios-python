# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como
# parâmetro e devolve o maior número primo menor ou igual ao número passado à função.
def éPrimo(k):
    for c in range(2, num):
        primo = 0
        if not c % 2 == 0:
            primo = primo + c
    print(f'O maior valor do número primo encontrado é {primo}')


num = int(input('Digite um número: '))
éPrimo(num)
