from main import *

house_price = float(input('Informe o valor da casa: '))
salary = float(input('Informe o seu salário: '))
payment_time = int(input('Em quanto anos vai ser pago a casa: '))

valuePerMouth = house_price / (payment_time * 12)

thirtyValue = salary * 0.30

if thirtyValue < valuePerMouth:
    print('\nO Valor da parcela ultrapassou 30% da sua renda')
    print(f"EMPRÉSTIMO {cores['red']}NEGADO{cores['lmp']}")

else:
    print(f'\n{cores["green"]}PARABÉNS{cores["lmp"]} o empréstimo foi aceito!')
    print('O valor da parcela seria R$ {}{:.2f}{}'.format(cores["yel"], valuePerMouth, cores["lmp"]))
