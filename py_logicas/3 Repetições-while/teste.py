# c = 1
# while c < 10:
#     print(c)
#     c = c + 1
# print('fim')

# n = 1
# while n != 0:
#     n = int(input('Digite: '))
# print('fim')

# r = 'S'
# while r == 'S':
#     n = int(input('Digite: '))
#     r = str(input('Continuo? ')).upper()
# print('fim')

par = 0
impar = 0
n = 1
while n != 0:
    n = int(input('Digite: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Foram {} números pares digitados e {} números ímpares!'.format(par, impar))