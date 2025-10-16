'''CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL MOSTRE QUANTAS PESSOAS AINDA NAO
ATINGIRAM A MAIORIDADE E QUANTAS JA SAO MAIORES. MAIORIDADE DE 21 ANOS'''

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em qual ano a {} pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >=21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E o total de {} menores de idade.'.format(totmenor))
