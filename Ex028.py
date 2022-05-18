from random import randint
from time import sleep

print('=-=' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('=-=' * 20)


while True:
    num = randint(0, 5)
    ans = int(input('Em que número eu pensei?(SE QUISER SAIR   DIGITE 9) '))

    print('PROCESSANDO...')
    sleep(2)
    if ans == 9:
        print(' === MUITO OBRIGADO POR JOGAR === ')
        break
    print('PARABÉNS! Você Conseguiu me vencer!' if ans == num else 'Tente NOVAMENTE!!!!')
