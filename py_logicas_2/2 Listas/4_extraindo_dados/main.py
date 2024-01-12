lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    lista.sort(reverse=True)
    resp = str(input('Continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-'*50)
print(f'Quantidade de números digitados: {len(lista)}.')
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')