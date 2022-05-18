import math
num = int(input('Informe um número(entre 0 e 9999): '))

print('Analisando o número {}'.format(num))


un = num // 1 % 10
de = num // 10 % 10
ce = num // 100 % 10
mi = num // 1000 % 10

print('unidade: {}'.format(un))
print('Dezena: {}'.format(de))
print('Centena: {}'.format(ce))
print('Milhar: {}'.format(mi))