from random import choice

alu1 = input('Informe o nome do aluno 1: ')
alu2 = input('Informe o nome do aluno 2: ')
alu3 = input('Informe o nome do aluno 3: ')
alu4 = input('Informe o nome do aluno 4: ')

lista = [alu1, alu2, alu3, alu4]

sorteado = choice(lista)

print('O sorteado para apag ar o quadro foi: {}'.format(sorteado))