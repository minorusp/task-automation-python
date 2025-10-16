'''REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NUMERO QUE O USUARIO ESCOLHER, SO QUE AGORA UTILIZANDO UM LAÇO FOR'''

numero = int(input('Digite o número da tabuada desejada: '))
print(f'\nTabuada de {numero}:')
for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')

'''except ValueError:
    print('Entrada inválida. Por favor, digite um número inteiro.')'''
