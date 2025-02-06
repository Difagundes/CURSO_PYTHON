'''

Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x e X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - centro
Sinal - + ou -
Ex.: 0>-100, .1f
Conversion flags - !r !s !a

'''
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000000000000.34347834768347:,.2f}')
print(f'O hexadecimal de 1500 {1500:04X}')