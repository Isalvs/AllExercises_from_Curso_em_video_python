travelKm = float(input('Quantos Quilometros vão ser percorridos nessa viagem? '))

if travelKm <= 200:
    travelKm = travelKm * 0.5
    print('O valor total da viagem vai ser: R${:.2f}'.format(travelKm))
else:
    travelKm = travelKm * 0.45
    print('O valor total da viagem vai ser: R${:.2f}'.format(travelKm))