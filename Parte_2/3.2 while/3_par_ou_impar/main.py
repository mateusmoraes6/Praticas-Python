from random import randint
computador = randint(0, 10)
cont = 0

print('VAMOS JOGAR ÍMPAR OU PAR!')
while True:
    print('*' * 25)
    valor = int(input('Diga um valor: '))
    parOuImpar = str(input('Par ou Ímpar? [P/I] ')).upper()
    print('-' * 25)
    soma = computador + valor
    if parOuImpar == 'P':
        if soma %2 == 0:
            print(f'Você jogou {valor} e o computador {computador}. Total de {soma} que é PAR!')
            print('-' * 25)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            cont += 1
        elif soma %2 == 1:
            print(f'Você jogou {valor} e o computador {computador}. Total de {soma} que é ÌMPAR!')
            print('Você PERDEU!')
            print('-' * 25)
            print(f'GAMER OVER! Você venceu {cont} vezes.')
            break
    elif parOuImpar == 'I':
        if soma %2 == 0:
            print(f'Você jogou {valor} e o computador {computador}. E o total é {soma}, que é PAR!')
            print('Você PERDEU!')
            print('-' * 25)
            print(f'GAMER OVER! Você venceu {cont} vezes.')
            break
        elif soma %2 == 1:
            print(f'Você jogou {valor} e o computador {computador}. E o total é {soma}, que é ÌMPAR!')
            print('-' * 25)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            cont += 1
