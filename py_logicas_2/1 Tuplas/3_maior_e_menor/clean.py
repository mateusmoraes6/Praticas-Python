from random import randint
numAleatórios = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print(f'Os valores sorteados foram: ', end='')
for n in numAleatórios:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numAleatórios)}.')
print(f'O menor número sorteado foi {min(numAleatórios)}.')
