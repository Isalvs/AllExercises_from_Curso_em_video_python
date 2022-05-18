from datetime import datetime

age = int(input('Informe a sua data de nascimento: '))

dt = datetime.now()


service = dt.year - age
lastTime = 18 - (dt.year - age)
lostTime = (dt.year - age) - 18

# print(dt.year - age)
# print(lastTime)

if service == 18:
    print('Vamos! Está na hora de se alistar!!')
elif service > 18:
    ano = dt.year - lostTime
    print('Seu alistamento foi em {}'.format(ano))
    print(f'Moscando soldado? Já passou {lostTime} anos  ')
elif service < 18:
    ano = dt.year + lastTime
    print(f'Seu alistamento será em {ano}')
    print(f'Calma cadete! Ainda falta {lastTime} anos para você se alistar!')
