#desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario se elas
#podem formar um triangulo
print('-='*14)
print('Analisador de Triângulos')
print('-='*14)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
