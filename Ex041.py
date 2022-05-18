from datetime import datetime

year = int(input('Informe o ano de seu nascimento: '))

dt = datetime.now()

age = dt.year - year

print(age)

if age <= 9:
    print('CATEGORIA: Mirim')

# 14 <= age <= 10
elif 14 >= age or age <= 10:
    print('CATEGORIA: Infatil')

elif 19 >= age or age <= 15:
    print('CATEGORIA: Junior')

elif 20 >= age:
    print('CATEGORIA: Sênior')

elif age > 20:
    print('CATEGORIA: Master')
