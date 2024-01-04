# from datetime import date
# data = date.today().year
# idades = []
# idadeAtingida = []
# idadeNaoAtingida = []

# for c in range(0, 3):
#     nasc = int(input('Seu ano de nascimento: '))
#     idades = data - nasc
#     idades.append(nasc)
# if nasc < 18:
#     idadeNaoAtingida.append(nasc)
#     print(idadeNaoAtingida)
# else:
#     idadeAtingida.append(nasc)
#     print(idadeNaoAtingida)

# Forma com menos linhas
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input(' Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E também tivemos {} pessoas maenores de idade.'.format(totmenor))
