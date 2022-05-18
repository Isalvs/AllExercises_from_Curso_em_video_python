vel = float(input('Digite a velocidade do carro que passou: '))

if vel > 80:
    vel = (vel - 80) * 7
    print('O motorista deve receber uma multa no valor de R${:.2f}!!'.format(vel))
else:
    print('Pode seguir viagem!!!')

