print('-' * 60)
print('Tente adivinhar um número entre 0 e 10 que estou pensando...')
print('-' * 60)

from random import randint
computador = randint(0, 3)
cont = 0
c = 'S'
stop = 'N'
while c == 'S':
    jogador = int(input('Tente adivinhar: '))
    if jogador == computador:
        print('ACERTOU!')
        cont += 1
        c = ('N')
    else:
        print('ERROU!')
        c = str(input('Pressione (S) para continuar ou (N) para desistir: ')).upper()
        cont += 1
print('Você tentou {} vezes adivinhar o número {}, que foi o que pensei.'.format(cont, computador))
