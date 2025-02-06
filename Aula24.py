# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4
#  D i e g o
# -5-4-3-2-1
'''
nome = 'Diego'

print(nome[2])
print(nome[-3])

print('ego' in nome)
print('di' not in nome)
'''
nome = input('Digite seu nome: ')
encontrar = input('Digite o que quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome} ')