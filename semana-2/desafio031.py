#desenvolva um programa que pergunte a distancia de uma viagem em km
#calcule o preço da passagem cobrando 0,50 por km rodado para viagens até
#200km e 0,45 para viagens mais longas

distancia = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
    print('O preço da passagem é R$ {:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('O preço da passagem é R$ {:.2f}'.format(preco))

