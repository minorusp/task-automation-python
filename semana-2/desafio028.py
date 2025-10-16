#escreva um programa que faça o computador pensar em um numero inteiro
# entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero
#escolhido pelo computador. o programa devera escrever na tela se o usuario
#venceu ou perdeu


import random
chutealeatorio = random.randint(0,5)
chute = int(input('Tente descobrir qual número entre 0 e 5 foi sorteado pelo computador: '))
if chutealeatorio == chute:
    print('Você venceu!')
else:
    print('Você perdeu! O número sorteado foi {}'.format(chutealeatorio))
