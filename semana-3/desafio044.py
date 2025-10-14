'''elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de
pagamento
a vista dinheiro/pix 10% de desconto
a vista cartao 5% desconto
ate 2x cartao preço normal
3x ou mais no cartao 20% de juros'''

print('{:=^40}'.format(' LOJAS GUANABARA '))
produto = float(input('Valor total da compra: R$ '))
print('''FORMAs DE PAGAMENTO
[1] à vista dinheiro/PIX
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input(' Qual a forma de pagamento? '))
if opção == 1:
    total = produto - (produto * 10 / 100)
elif opção == 2:
    total = produto - (produto * 5 / 100)
elif opção == 3:
    total = produto
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} reais.'.format(parcela))
elif opção == 4:
    total = produto + (produto * 20 / 100)
    totalparcela = int(input('Quantas parcelas? '))
    parcela = total / totalparcela
    print('Sua compra será parcelada em {}x de R$ {:.2f} reais.'.format(totalparcela, parcela))
else:
    total = produto
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente. ')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(produto, total))

