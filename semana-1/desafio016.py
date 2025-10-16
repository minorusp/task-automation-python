# crie um programa que leia um numero real qualquer pelo teclado e mostre na telq
# a sua porção inteira, ex: digite um numero 6.127 o numero 6.127 tem a parte inteira 6
import math
num = float(input('Digite um valor: '))
print ('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))
