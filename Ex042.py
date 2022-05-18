from main import cores

while True:
    r1 = float(input('Informe o comprimento de uma reta: '))
    r2 = float(input('Informe o comprimento de outra reta: '))
    r3 = float(input('Informe o comprimento de outra reta: '))

    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('É um {}Triangulo!!{}'.format(cores['green'], cores['lmp']))
        if r1 == r2 == r3:
            print('Triângulo Equilátero')

        elif r1 != r2 != r3 != r1:
            print('Triângulo Escanleno')

        else:
            print('Triângulo Isóscles')

    else:
        print('Não é um TRIÂNGULO')

    print('\n\nDeseja continuar? (1 - para continuar / 2 para sair)')
    cont = int(input('--> '))

    if cont == 1:
        print('\n\n\n\n\n')
        continue
        print()

    elif cont == 2:
        break
