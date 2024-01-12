números = list()
while True:
    valor = (int(input('Digite um valor: ')))
    if valor not in números:
        números.append(valor)
    else:
        print('Valor Duplicado! Não adicionado.')
    r = str(input('Continuar? [S/N] '))
    if r in 'Nn':
        break
print('-'*50)
números.sort()
print(f'Você digitou os valores: {números}.')