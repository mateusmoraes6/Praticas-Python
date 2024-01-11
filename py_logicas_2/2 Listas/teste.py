# num = [2, 5, 9, 1, 7, 10, 3]
# num[2] = 3
# num.append(8)
# num.sort(reverse=True)
# num.insert(2, 0)
# num.pop(2)
# if 7 in num:
#     num.remove(7)
# else:
#     print('Não achei')
# print(num)
# print(f'Quantidade de elementos na ista: {len(num)}')

valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

# # for v in valores:
# #     print(f'{v}...', end=' ')

for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}')
print('Fim')

# a = [4, 6, 7, 3, 9]
# b = a [:]
# b[3] = 300
# print(f'Lista A: {a}') # [4, 6, 7, 3, 9]
# print(f'Lista B: {b}') # [4, 6, 7, 300, 9]