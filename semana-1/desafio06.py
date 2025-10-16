#crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
n = int (input ('Digite um número:'))
d = n * 2
t = n * 3
r = n ** (1/2)
print ("O dobro do número digitado é: {}, o triplo é {} e a raiz quadrada {:.2f}".format(d,t,r))
