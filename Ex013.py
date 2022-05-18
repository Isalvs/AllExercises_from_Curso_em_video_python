import emoji

salario = float(input('Qual o salário de um funcionário? R$'))
ajustado = salario + (salario*0.15)

print(emoji.emojize('Um funcionário que ganhava {:.2f}, com 15% de aumento, passa a receber R${:.2f}:flushed:'.format(salario, ajustado), language='alias'))