from datetime import datetime

anoNascimento = int(input('Informe o ano que você nasceu: '))

dataAtual = datetime.now()

idade = dataAtual.year - anoNascimento
print(idade)

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR') 
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')