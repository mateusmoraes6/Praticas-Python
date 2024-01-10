from random import randint
num = 5
numAleatórios = [randint(1, 20) for c in range(num)]
print(f'Os valores sorteados foram: {numAleatórios}')
print(f'O maior valor sorteado foi {max(numAleatórios)}.')
print(f'O menor número sorteado foi {min(numAleatórios)}.')
