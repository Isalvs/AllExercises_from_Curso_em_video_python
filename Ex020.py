from random import shuffle

grp1 = input('Lider grupo 1:')
grp2 = input('Lider grupo 2:')
grp3 = input('Lider grupo 3:')
grp4 = input('Lider grupo 4:')

lista = [grp1, grp2, grp3, grp4]
print(lista)
shuffle(lista)
print(lista)

