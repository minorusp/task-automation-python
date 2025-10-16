#faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
produto = float(input('Digite o valor do produto: R$ '))
desconto = produto*5/100
resultado = produto - desconto
print('O novo valor desse produto com 5% de desconto é: {:.2f}'.format(resultado))
