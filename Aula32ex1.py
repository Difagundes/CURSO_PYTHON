'''

Faça um programa que peça ao usuário para digitar im número inteiro, informe se este número é par ou impar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.

'''

numero = input('Digite um número inteiro: ')

try:
    num_float = float(numero)
    num_int = int(num_float)
    num_e_int = (num_float - num_int) == 0
    if num_e_int:
        if (num_int % 2) == 0:
            print(f'{numero=} digitado é par.')
        else:
            print(f'{numero=} digitado é impar.')
    else:
        print('Número digitado não é inteiro.')
except:
    print('Você não digitou um numero.')