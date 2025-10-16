'''FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS DE ARTIFICIO
INDO DE 10 ATE 0, COM UMA PAUSA DE 1SEGUNDO ENTRE ELES'''

from time import sleep
print('{} CONTAGEM REGRESSIVA {}'.format('-=-' *1, '-=-' *1,))
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\N{FIREWORKS}')

