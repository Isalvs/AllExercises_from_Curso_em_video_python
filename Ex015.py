
day = int(input('Por quantos dias ficou com o carro? '))
km = float(input('Quantos km rodou? '))

#traveledKm = 0.15
#traveledDay = 60
#totalPKm = km * traveledKm
#totalPDay = day * traveledDay
#amount = totalPDay + totalPKm

amount = (day * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(amount))
