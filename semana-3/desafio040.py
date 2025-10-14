''''crie um programa que leia duas notas de um aluno e calcule sua media mostrando uma msg final de acordo com a media
atingida
media abaixo de 5.0: REPROVADO
media entre 5.0 e 6.9: RECUPERAÇÃO
media 7.0 ou superior: APROVADO'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Sua nota média foi {} e você foi REPROVADO!'.format(media))
elif 5 <= media < 6.9:
    print('Sua nota média foi {} e você está de RECUPERAÇÃO!'.format(media))
else:
    print('Sua nota média foi {} e você foi APROVADO!'.format(media))
