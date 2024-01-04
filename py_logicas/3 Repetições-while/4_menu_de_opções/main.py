novoNums = 4
sairDoPrograma = 5

while novoNums == 4 or sairDoPrograma != 5:
    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))
    print(v1, v2)

    print('veja as opções abaixo e escolha uma ação:')
    print('''AÇÕES:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    decisão = int(input('O que você quer que eu faça? '))

    if decisão == 1:
        soma = v1 + v2
        print('A soma entre {} e {} é igual a {}.'.format(v1, v2, soma))
    elif decisão == 2:
        mult = v1 * v2
        print('A multiplicação entre {} e {} é igual a {}.'.format(v1, v2, mult))
    elif decisão == 3:
        if v1 != v2:
            maior = max(v1, v2)
            print('O maior número entre {} e {} é o número {}.'.format(v1, v2, maior))
        if v1 == v2:
            print('Os números que você forneceu são iguais: {} e {}'.format(v1, v2))
    elif decisão == 4:
        print('Digite novos números...')
    elif decisão == 5:
        print('Você saiu do prgrama!')
        break
    else:
        print('Valor inválido, tente novamente...')
