# CODIO LIMPO  

velocidade= 66
local_carro = 101

RADAR = 60
LOCAL_1 = 100
RANGE = 1

velocidade_acima = velocidade>60
passou_no_radar = local_carro==(LOCAL_1-RANGE) or local_carro==(LOCAL_1+RANGE)

if velocidade_acima and passou_no_radar :
    print('O carro foi multado')
else:
    print('O carro não foi multado!')
   