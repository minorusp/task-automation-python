'''escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. o programaq vai perguntar o valor da casa,
o salario do comprador e em quantos anos ele vai pagar. calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do
salário ou entao o emprestimo sera negado'''
'''qual valor da casa?, qual o salário?, qual prazo de pagamento?'''
'''qual valor da prestação?, prestação não pode ser maior que 30% do salário!'''

valor_casa = float(input('Qual o valor da casa? R$ '))
sal = float(input('Qual o salario do comprador? R$ '))
prazo = int(input('Em quantos anos vai pagar? '))
valor_parcela = valor_casa / (prazo * 12)
limite_prestacao = sal *0.30
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(valor_casa, prazo))
print('O valor da parcela será de R$ {:.2f}'.format(valor_parcela))
if (valor_parcela <= limite_prestacao):
    print('O financiamento do imóvel foi aprovado!')
else:
    print('O financimento foi recusado!')




