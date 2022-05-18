from main import *

print('===== Avaliador automático =====')
print()

n1 = float(input('Informe a nota 1: '))
n2 = float(input('Informe a nota 2: '))

media = (n1 + n2) / 2

if media >= 7:
    print("\n{} PARABÉNS !!{} A média alcançada foi de {:.2f}".format(cores['green'], cores['lmp'], media))

elif 6.9 >= media >= 5:
    print('\n{} RECUPERAÇÃO !! {} A média alcançada foi de {:.2f}'.format(cores['yel'], cores['lmp'], media))

elif media < 5:
    print('\n{} REPROVADO !! {} A média alcançada foi de {:.2f}'.format(cores['red'], cores['lmp'], media))