from math import hypot

catOp = float(input('Informe o cateto oposto do triângulo: '))
catAd = float(input('Informe o cateto adjacente do triângulo: '))

hipo = hypot(catOp, catAd)

print('O comprimento da Hipotenusa é igual a: {:.2f}'.format(hipo))


