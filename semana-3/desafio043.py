'''desenvolva uma logica que leia o peso e a altura de uma pessoa e calcule seu IMC e mostre seu status de acordo com a tabela
abaixo de 18.5 abaixo do peso
entre 18.5 e 25 peso ideal
25 ate 30 sobrepeso
30 ate 40 obesdade
acima de 40 obesidade morbida'''

peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura em METROS: '))
imc: float = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é de {:.1f} e você está ABAIXO do peso!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é de {:.1f} e você está no peso IDEAL!'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é de {:.1f} e você está com SOBREPESO!'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é de {:.1f} e você está com OBESIDADE!'.format(imc))
else:
    print('Seu IMC é de {:.1f} e você está com OBESIDADE MÓRBIDA!'.format(imc))

