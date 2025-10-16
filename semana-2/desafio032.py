#faça um programa que leia um ano qualquer e mostre se é um ano bisexto

from calendar import isleap
ano = int(input('Digite o ano que deseja analisar: '))
if isleap(ano):
    print('{} é um ano BISSEXTO!'.format(ano))
else:
    print('{} não é um ano BISSEXTO!'.format(ano))
