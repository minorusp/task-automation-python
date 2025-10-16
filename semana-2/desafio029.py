#escreva um programa que leia a velocidade de um carro, se ele ultrapassar
#a velocidade de 80km/h mostre uma msg dizendo que ele foi multado
#a multa vai custar R$7,00 por cada km acima do limite

carro = float(input('Qual a velocidade atual do carro? '))
if carro > 80:
    print('Você foi multado por excesso de velocidade e o valor da multa é: R${}'.format((carro - 80) * 7))
else: print('Parabéns você respeitou os limites de velocidade!')
