name = input('Digite seu nome completo: ').strip()

print('Seu nome com todas as letras maiusculas fica: {}'.format(name.upper()))
print('Seu nome com todas as letras minusculas fica: {}'.format(name.lower()))

print('Seu nome tem ao todo {} letras'.format(len(name) - name.count(' ')))
firstSpace = name.find(' ')

separa = name.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
