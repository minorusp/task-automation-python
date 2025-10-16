# faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento
salario = float(input('Digite o valor do seu salário: R$ '))
aumento = salario * 15/100
resultado = salario + aumento
print ('O seu novo salário com reajuste de 15% é de: R$ {:.2f}'.format(resultado))
