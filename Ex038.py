from main import *

while True:
    num1 = int(input('Insira um número -> '))
    num2 = int(input('Insira outro número -> '))

    if num1 > num2:
        print('O primeiro valor é maior!')
    elif num2 > num1:
        print('O segundo valor é maior!')
    elif num1 == num2:
        print('Não existe valor maior, os dois são iguais!')
    else:
        print('Números???')

    print('\n\n\n')

    print(f'Deseja sair??? (1 - {cores["green"]}Continuar{cores["lmp"]}/ 2 - {cores["red"]}Sair{cores["lmp"]})')
    exit = int(input('--> '))
    if exit == 1:
        continue
    elif exit == 2:
        break

    print()

print('\n\n\n')
print('Obrigado por usar nosso programa!')