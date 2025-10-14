'''faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade:
se ele ainda vai ter que se alistar
se é a hora de se alistar
se ele ja passou do tempo de se alistar
o programa tambem devera mostrar quanto tempo falta ou se ele ja passou do prazo de alistamento'''

from datetime import date
nascimento = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - nascimento
if idade == 18:
    print('Você tem {} anos e deverá se alistar!'.format(idade))
elif idade < 18:
    print('Você tem {} anos deverá se alistar daqui a {} anos.!'.format(idade, 18 - idade))
else:
    print('Você ja passou {} anos do prazo de alistamento.'.format(idade -18))
