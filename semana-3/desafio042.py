'''refaça o desafio 035 dos triangulos acrescentando o recurso de mostrar que tipo de triangulo sera formado
equilatero, todos os lados iguais
isosceles, dois lados iguais
escaleno, todos os lados diferentes'''

r1 = float(input('Digite o primeito segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triangulo!', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 !=r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIANGULO!')
