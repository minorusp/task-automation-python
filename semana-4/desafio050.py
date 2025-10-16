'''DESENVOLVA UM PROGRAMA QUE LEIA 6 NUMEROS INTEIROS QUE MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES.SE O VALOR
DIGITADO FOR IMPAR DESCONSIDERE-O'''

soma_pares = 0
print('{} Digite 6 números inteiros {}'.format('=-' *3, '=-' *3))
for i in range(1, 7):
    try:
        numero = int(input(f'Digite um número:'))
        if numero % 2 == 0:
            soma_pares += numero
    except ValueError:
        print('Entrada inválida. Por favor, digite um número inteiro')
print(f'\nA soma de todos os números PARES digitados é: {soma_pares}')
print('-' * 20)
