#escreva um programa que leia um valor em metros e o exiba convertido em centrimeros e milimetros
t = float(input('Digite o número em metros a ser convertido:'))
print ("São {:.0f} centímetros e {:.0f} milimetros". format (t * 100, t * 1000))
