novoNums = 4
continua = 'S'
lista = []

while novoNums == 4:

    while continua == 'S':
        valores = int(input('Digite o valor: '))
        lista.append(valores)
        continua = str(input('(S) adiciona mais e (N) escolhe avaliá-los: ')).upper()
        if continua != 'S':
            print('\nSeus valores: {}.\n'.format(lista))

    print('Escolha uma ação abaixo:')
    print('''Suas opções:
    [ 1 ] Média
    [ 2 ] Maior/Menor
    [ 3 ] Análise completa
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    decisão = int(input('O que você quer que eu faça? '))

    if decisão == 1:
        media = sum(lista) / len(lista)
        print('A média dos valores: {}, foi de {}.'.format(lista, media))
        break
    elif decisão == 2:
        maior = max(lista)
        menor = min(lista)
        print('O maior número dessa sequência é {} e o menor é {}.'.format(maior, menor))
        break
    elif decisão == 3:
        media = sum(lista) / len(lista)
        maior = max(lista)
        menor = min(lista)
        print('O maior número dessa sequência é {} e o menor é {} e a sua média entre os valores foi {:.2f}.'.format(maior, menor, media))
        break
    elif decisão == 4:
        print('Digite novos números...')
    elif decisão == 5:
        print('Você escolheu sair do programa!')
        break
    else:
        print('Por favor, digite um valor válido!')