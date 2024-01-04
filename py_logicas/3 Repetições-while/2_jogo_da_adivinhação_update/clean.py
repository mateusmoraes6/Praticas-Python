from random import randint
computador = randint(0, 10)
print('Sou o computador e acabei de pensar em um número entre 0 e 10...')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente outra vez.')
        elif jogador > computador:
            print('Menos... tente outra vez.')
print('Acertou com {} tentativas!!!!'.format(palpites))