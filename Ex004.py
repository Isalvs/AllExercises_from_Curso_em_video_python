

var = input('Digite algo: ')

print('o tipo primitivo desse valor é: {}'.format(type(var)))
print('Só tem espaços? {}'.format(var.isspace()))
print('É um número? {}'.format(var.isnumeric()))
print('É alfabético? {}'.format(var.isalpha()))
print('É um alfanumérico? {}'.format(var.isalnum()))
print('Está em maiúsculas? {}'.format(var.isupper()))
print('Está em minúsculas? {}'.format(var.islower()))
print('Está capitalizada? {}'.format((var.istitle())))