a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = a1 + (10 - 1) * r
for c in range(a1, decimo + r, r):
    print('{} '.format(c), end='-> ')
print('Pronto.')
