# Interrompendo repetições while: break
# n = s = 0
# while True:
#     n = int(input('Digite um número: '))
#     if n == 999:
#         break
#     s += n
# print('A soma vale {}.'.format(s))

# Mudando a formatação das strings com fstrings
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}.')