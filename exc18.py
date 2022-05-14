#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. #
import math
ang = int(input('Digite o valor do ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tag = math.tan(math.radians(ang))
print('O seno de {} é igual a: {:.2f}, o cosseno é igual a: {:.2f} e a tangente igual a: {:.2f}'.format(
    ang, sen, cos, tag))
