lista = []
pares = []
ímpares = []
c = 'S'
while c == 'S':
    num = (int(input('Digite um valor: ')))
    if lista.count(num) > 0:
        print('Valor Duplicado! Não adicionado.')
    else:
        lista.append(num)
        if num % 2 == 0:
            pares.append(num)
        else:
            ímpares.append(num)
        print('Valor adicionado.')
    c = str(input('Continuar? [S/N] ')).upper()
print('-'*50)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {ímpares}')