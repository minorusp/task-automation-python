#crie um programa que leia um numero inteiro e mostre na tela se ele é
#par ou impar

numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print('O número {} é PAR!'.format(numero))
else: print('O número {} é ÍMPAR!'.format(numero))