print(' ===== CONDICIONOMETRO ===== \n')

average_price = float(input('Informe o valor do produto em R$: '))

payment_type = int(input('''

Informe o metódo de pagamento:

1 - À vista (Dinheiro / cheque)
2 - À vista no cartão
3 - 2x no cartão
4 - 3x ou mais no cartão

-> '''))

if payment_type == 1:
    desc = average_price * 0.10
    average_price = average_price - desc
    print('Com um desconto de 10%')
    print('O valor do produto será R${:.2f}'.format(average_price))

elif payment_type == 2:
    desc = average_price * 0.05
    average_price = average_price - desc
    print('Com um desconto de 5%')
    print('O valor do produto será R${:.2f}'.format(average_price))

elif payment_type == 3:
    print('Não há desconto para este metódo de pagamento')
    print('O valor do produto não muda, será R$ {:.2f}'.format(average_price))

elif payment_type == 4:
    qtd_parc = int(input('Em quantas parcelas? -> '))

    feesPrice = average_price * 0.20 * qtd_parc
    finalAmount = average_price + feesPrice
    print('Neste metódo de pagamento há 20% de juros para cada parcela')
    print('O valor final será de R$ {:.2f}'.format(finalAmount))
