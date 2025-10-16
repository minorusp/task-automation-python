'''DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZAO DE UMA PROGRESSAO ARITIMETICA. NO FINAL MOSTRE OS 10 PRIMEIROS TERMOS
DESSA PROGRESSAO'''


primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c),end=' → ')
print('ACABOU')

