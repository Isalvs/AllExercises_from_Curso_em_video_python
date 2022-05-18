price = float(input('Qual o preço do produto? '))

newPrice = price - (price * 0.05)

print('O preço do produto era {:.2f}, e com o reajuste vai custar {:.2f}'.format(price, newPrice))
