sal = float(input('Qual o seu salário? '))

if sal > 1250.00:
    salAum = sal + (sal * 0.10)
    print(f'Com o aumento de 10% o seu salário vai ficar {salAum}')

elif sal <= 1250.00:
    salAum = sal + (sal * 0.15)
    print(f'Com o aumento de 15% o seu salário vai ficar {salAum}')
