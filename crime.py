# 45)Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa
# responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
# e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
perguntas = []
print('-'*20)
print('Questionário - Responder S ou N ')
print('-'*20)
contpos = 0

p1 = str(input('Telefonou para a vítima? '))
perguntas.append(p1.lower())
p2 = str(input('Esteve no local do crime? '))
perguntas.append(p2.lower())
p3 = str(input('Mora perto da vítima? '))
perguntas.append(p3.lower())
p4 = str(input('Devia para a vítima? '))
perguntas.append(p4.lower())
p5 = str(input('Já trabalhou para a vítima? '))
perguntas.append(p5.lower())

for c in perguntas:
    if c == 's':
        contpos += 1

if contpos == 2:
    print('Você é suspeito.')
elif contpos == 3:
    print('Você é cúmplice.')
elif contpos == 5:
    print('Você é assassino.')
else:
    print('Você é inocente!')
