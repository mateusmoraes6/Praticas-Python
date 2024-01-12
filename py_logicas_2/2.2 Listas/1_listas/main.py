pessoas = list()
dados = list()
cont = 0
while True:
    nome = str(input('Nome: '))
    cont += 1
    peso = float(input('Peso: '))
    continua = str(input('Quer continuar? [S/N] '))
    if continua in 'Nn':
        break
print('Total de pessoas cadastradas: {cont}.')