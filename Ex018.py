from math import cos, sin, tan, radians


ang = float(input('Digite um valor para o ângulo: '))


sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print('O valor do cosseno é: {:.2f} \nO valor do seno é: {:.2f} \nE o valor da Tangente é: {:.2f}'.format(cos, sen, tan))
