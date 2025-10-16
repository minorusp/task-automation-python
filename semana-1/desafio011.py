#1faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta
# necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m2

a = float(input('Digite a altura:'))
l = float(input('Digite a largura:'))
c = (a*l)
c1 = c/2
print ('Você precisa de {} litros de tinta' .format(c1))
