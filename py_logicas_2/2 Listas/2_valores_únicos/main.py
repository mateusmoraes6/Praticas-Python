lista = []
c = 'S'
while c == 'S':
    valor = (int(input('Digite um valor: ')))
    if lista.count(valor) > 0:
        print('Valor Duplicado! Não adicionado.')
    else:
        lista.append(valor)
        print('Valor adicionado.')
    c = str(input('Continuar? [S/N] ')).upper()
print('-'*50)
print(f'Você digitou os valores: {sorted(lista)}.')