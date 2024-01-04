contIdade = contMasc = contFem = 0
continua = 'S'
while continua == 'S':
    print('-' * 30)
    print('     CADASTRO DE PESSOAS')
    print('-' * 30)
    idade = int(input('Idade: '))
    while idade <= 0:
        idade = int(input('Idade: '))
    if idade >= 18:
        contIdade += 1
    sexo = str(input('Sexo: [M/F] ')).upper()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).upper()
    if sexo == 'M':
        contMasc += 1
    elif sexo == 'F' and idade < 20:
        contFem += 1
    print('-' * 30)
    continua = str(input('Continuar cadastro? [S/N] ')).upper()
    while continua != 'S' and continua != 'N':
        continua = str(input('Continuar cadastro? [S/N] ')).upper()
print('-' * 30)
print('     CADASTRO ENCERRADO')
print('-' * 30)
print(f'''Total de pessoas com 18 anos ou mais: {contIdade}.
Total de homens cadastrados: {contMasc}.
Total de mulheres com menos de 20 anos: {contFem}.''')
