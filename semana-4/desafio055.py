'''FAÇA UM PROGRAMA QUE LEIA O PESO DE 5 PESSOAS E NO FINAL MOSTRE QUAL FOI O MAIOR E O MENOR PESO'''

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa em Kg: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
                menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))
