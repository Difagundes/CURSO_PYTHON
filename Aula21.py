# Operadores lógicos: and (e) / or (ou) / not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressao interia sera avaliada naquele valor.
# São considerados falsy (que ja foi visto): 0 / 0.0 / '' / False.
# Também existe o tipo None que é usado para representar um não valor.

entrada = input('[E]Entrar ou [S]Sair: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrou')
elif entrada == 'E' and senha_permitida != senha_digitada:
    print('Senha incorreta')
elif entrada == 'S':
    print('Saiu')
else:
    print('Opção incorreta')