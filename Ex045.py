from random import randint
from time import sleep

import os

print(' ===== VAMOS JOGAR JOKENPÔ ===== ')
while True:

    player = int(input('''
    
1 - PEDRA
2 - PAPEL
3 - TESOURA
    
--> '''))

    machine = randint(1, 3)
    print()
    print('JO\n')
    sleep(0.5)
    print('KEN\n')
    sleep(0.75)
    print('PÔ!!\n')
    sleep(1)

    print('\n')

    # Condição de EMPATE

    if machine == 1 and player == 1 or machine == 2 and player == 2 or machine == 3 and player == 3:
        print('EMPATE')

    # Condições para o Jogador ganhar ->

    elif machine == 1 and player == 2:
        print('A máquina jogou PEDRA')
        print('Jogador Ganhou!')

    elif machine == 2 and player == 3:
        print('A máquina jogou PAPEL')
        print('Jogador Ganhou!')

    elif machine == 3 and player == 1:
        print('A máquina jogou TESOURA')
        print('Jogador Ganhou!')


    # Condições para a Máquina ganhar ->

    elif machine == 2 and player == 1:
        print('A máquina jogou PAPEL')
        print('Máquina Ganhou!')

    elif machine == 3 and player == 2:
        print('A máquina jogou TESOURA')
        print('Máquina Ganhou')

    elif machine == 1 and player == 3:
        print('A máquina jogou PEDRA')
        print('Máqunia Ganhou')

    print()

    os.system('PAUSE')

    print('\nDeseja continuar? (1 - para sim / 2 - para não)')
    cont = int(input('-> '))

    if cont == 2:
        break
        print('Obrigado por Jogar com a gente')
    else:
        continue
