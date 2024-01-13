pares = list()
ímpares = list()
for c in range(0, 7):
    c += 1
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        pares.append(num)
    if num %2 == 1:
        ímpares.append(num)
print('-'*48)
print(f'Os valores pares digitados foram: {sorted(pares)}')
print(f'Os valores ímpares digitados foram: {sorted(ímpares)}')