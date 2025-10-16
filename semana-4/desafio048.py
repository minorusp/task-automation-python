'''FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NUMEROS IMPARES QUE SAO MULTIPLOS DE 3 E QUE SE ENCONTREM NO
INTERVALO DE 1 ATE 500'''

multiplos_de_3 = []
soma = 0
cont = 0
for numero in range(1, 501, 2):
    if numero % 3 == 0:
        cont = cont + 1
        soma = soma + numero
print('A soma de todos os {} valores solicitados: {}'.format(cont, soma))
