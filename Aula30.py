'''

CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)

'''

velocidade = 61 # Velocidade atual do carro
local_carro = 100 # Local que o carro eatá na estrada

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # Alcance do radar

vel_acima = velocidade > RADAR_1
alcance_radar = (LOCAL_1 - RADAR_RANGE), LOCAL_1, (LOCAL_1 + RADAR_RANGE)

if local_carro in alcance_radar:
    if vel_acima:
        print('Carro multado no radar 1!')
    else:
        print('Carro não foi multado no radar 1!')
else:
    if vel_acima:
        print('Carro acima da velocidade mas fora do alcance do radar 1.')
    else:
        print('Carro dentro da velocidade permitida.')