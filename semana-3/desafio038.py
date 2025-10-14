'''escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem.
o primeiro valor é maior
o segundo valor é maior
não existe valor maior, os dois são iguais'''

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
if valor1 == valor2:
    print('Os valores são IGUAIS!')
elif valor1 > valor2:
    print('O PRIMEIRO valor é maior!')
else:
    print('O SEGUNDO valor é maior')
