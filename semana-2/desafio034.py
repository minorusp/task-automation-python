#faça um programa que pergunte o salario de um funcionario e calcule o valor
#do seu aumento. Para salarios superiores a 1250 calcule um aumneto de 10%
#para salarios iguais ou inferiores o aumento é de 15%

salario = float(input('Qual o valor do seu salário R$: '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print('O valor do novo salário com aumento de 15% é de {:.2f}'.format(novo))
else:
    novo = salario + (salario * 10 / 100)
    print("O valor do novo salário com aumento de 10% é de {:.2f}".format(novo))