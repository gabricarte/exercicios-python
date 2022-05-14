# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. #
import math
co = int(input('Digite o valor do cateto oposto: '))
ca = int(input('Digite o valor do cateto adjacente: '))
hi = (math.sqrt(co)) + (math.sqrt(ca))
print('O valor da hipotenusa é {}'.format(hi))
