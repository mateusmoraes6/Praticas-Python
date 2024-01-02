from random import randint
computador = randint(0, 10)

valor = int(input('Diga um valor: '))
parOuImpar = str(input('Par ou Ímpar? [P/I] ')).upper()

soma = computador + valor

if parOuImpar == 'P':
    if soma %2 == 0:
        print(f'Você jogou {valor} e o computador {computador}. Total de {soma} que é PAR!')
    elif soma %2 == 1:
        print(f'Você jogou {valor} e o computador {computador}. Total de {soma} que é ÌMPAR!')
    print('Você VENCEU!')
    print('Vamos jogar novamente...')
elif parOuImpar == 'I':
    if soma %2 == 0:
        print(f'Você jogou {valor} e o computador {computador}. E o total é {soma}, que é PAR!')
    elif soma %2 == 1:
        print(f'Você jogou {valor} e o computador {computador}. E o total é {soma}, que é ÌMPAR!')
    print('Você PERDEU!')
    print('GAMER OVER!')

