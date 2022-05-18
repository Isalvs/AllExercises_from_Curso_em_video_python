
alt = float(input('Qual a altura da parede? '))
lag = float(input('Qual a largura da parede?'))

area = lag * alt

print ('A sua parede tem a dimensão de {}x{} e sua área é de {}m² '.format(lag, alt, area))

lata = area / 2

print('Para pintar essa parede vai ser necessário usar {}l de tinta'.format(lata))