'''CRIE UM PROGRAMA QUE LEIA UMA FRASE E DIGA SE ELA É UM PALINDROMO, DESCONSIDERANDO OS ESPAÇOS
EX: APOS A SOPA, A SACADA DA CASA, O LOBO AMA BOLO'''

frase = str(input('Digite uma frase: ')).strip().upper() #upper para caixa grande
palavras = frase.split() #elimina espaços
junto = ''.join(palavras) #retira os espaços
inverso = junto[::-1] #fatiamento de string
'''for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
