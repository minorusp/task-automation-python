nome = str(input('Digite seu nome completo: ')).strip()
idade = int(input('Digite sua idade: '))
calculo = 2025 - idade
calculo1 = idade + 1
print('Prazer em te conhecer {}, sua idade é {} anos, e você nasceu em {}.'.format(nome, idade, calculo ))
print('No próximo ano {} terá {} anos de idade! '.format(nome, calculo1))
