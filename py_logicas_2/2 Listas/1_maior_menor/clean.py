listaNum = []
mai = men = 0
for c in range(0, 5):
    listaNum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listaNum[c]
    else:
        if listaNum[c] > mai:
            mai = listaNum[c]
        if listaNum[c] < men:
            men = listaNum[c]
print('-'*40)
print(f'Você digitou os valores: {listaNum}.')
print(f'O maior valor digitado foi {mai} na posição: ', end='')
for i, v in enumerate(listaNum):
    if v == mai:
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {men} na posição: ', end='')
for i, v in enumerate(listaNum):
    if v == men:
        print(f'{i}... ', end='')
print()
