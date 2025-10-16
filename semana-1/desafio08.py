#escreva um programa que leia um valor em metros e o exiba convertido em centrimeros e milimetros
m = float(input('Digite o número em metros a ser convertido:'))
print ("São {:.0f} centímetros e {:.0f} milimetros". format (m* 100, m * 1000))
