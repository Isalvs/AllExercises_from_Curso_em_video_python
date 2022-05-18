from main import *

num = int(input('Insira um número para ser feita a conversão: '))
print()
ans = int(input('''
Insira um número para selecionar a base de conversão:

1 - para binário
2 - para octal
3 - para hexadecimal

-> '''))


if ans == 1:
    print('O número {} convertido para binário ficará {}!'.format(num, format(num, 'b')))

elif ans == 2:
    print('O número {} convertido para Octal ficará {}!'.format(num, format(num, 'o')))

elif ans == 3:
    print('O número {} convertido para  Hexadecimal ficará {}!'.format(num, format(num, 'x')))

else:
    print(f'Opção {cores["red"]}INVALIDA!{cores["lmp"]}')