#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#considere US$ 1,00 = R$3,27

carteira = float(input('Qual valor você tem na carteira? R$ '))
dólar = carteira/3.27
print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(carteira, dólar))