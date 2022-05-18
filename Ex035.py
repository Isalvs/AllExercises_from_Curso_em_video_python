from main import cores

r1 = float(input('Informe o comprimento de uma reta: '))
r2 = float(input('Informe o comprimento de outra reta: '))
r3 = float(input('Informe o comprimento de outra reta: '))

print(r1, r2, r3)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('é um {}triangulo!!{}'.format(cores['red'], cores['lmp']))
else:
    print('não É um TRIÂNGULO')
