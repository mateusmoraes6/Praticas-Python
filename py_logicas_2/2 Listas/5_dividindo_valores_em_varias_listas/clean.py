num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Continuar? [S/N] ')).upper()
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
        print('Valor adicionado.')
print('-'*50)
print(f'A lista completa é: {num}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {ímpares}')