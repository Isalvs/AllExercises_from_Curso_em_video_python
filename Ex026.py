frs = str(input('Digite uma Frase: ')).strip().lower()

print('A letra A aparece {} vezes na frase'.format(frs.count('a')))
print('A primeira letra A apareceu na posição {}!'.format(frs.find('a') + 1))
print('A última letra A apareceu na posição {}'.format(frs.rfind('a') + 1))
