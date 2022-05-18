import os

alt = float(input('Informe a sua altura: '))
peso = float(input('Informe o seu peso:'))

imc = peso / (alt**2)

print('Seu IMC é: {:.4f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso!')

elif imc < 25:
    print('Você está no peso ideal')

elif imc < 30:
    print('vocês está com sobrepeso!')

elif imc < 40:
    print('Vocês está com obesidade')

elif imc > 41:
    print('Você está com obesidade Mórbida')

os.system("PAUSE")