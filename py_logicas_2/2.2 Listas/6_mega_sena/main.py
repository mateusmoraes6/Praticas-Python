from random import randint
from time import sleep
palpites = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, palpites):
    c += 1
    num = [randint(1, 60) for r in range (6)] 
    sleep(0.5)
    print(f'Jogo {c}: {sorted(num)}')