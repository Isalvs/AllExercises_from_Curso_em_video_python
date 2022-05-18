from math import floor, trunc

num: float = float(input('Digite um número real (números com virgula): '))

print(round(num))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, floor(num)))
print((trunc(num)))
