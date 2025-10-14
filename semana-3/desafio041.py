'''a confederacao nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria de acordo com a idade

ate 9 anos mirim
ate 14 anos infantil
ate 19 anos junior
ate 20 anos senior
acima master'''

from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nascimento
if idade <= 9:
    print('Você tem {} anos e pertence a categoria MIRIM!'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e pertence a categoria INFANTIL!'.format(idade))
elif idade <= 19:
    print('Você tem {} anos e pertence a categoria JUNIOR!'.format(idade))
elif idade <= 20:
    print('Você tem {} anos e pertence a categoria SENIOR!'.format(idade))
else:
    print('Você tem {} anos e pertence a categoria MASTER'.format(idade))
