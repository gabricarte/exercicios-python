# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.#
valor = int(input('Digite o valor em metros: '))
cm = valor*100
mm = valor*1000
print('O valor de {} metros equivale a {} centímetros e {} milímetros'.format(
    valor, cm, mm))
