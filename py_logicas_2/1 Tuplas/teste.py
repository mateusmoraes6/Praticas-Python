# (Tuplas) [Listas] {Dicionários}

# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# print(sorted(lanche))
# # print(len(lanche))
# # print(lanche) # ('hamburguer', 'suco', 'pizza', 'pudim')
# # print(lanche[1]) # suco
# # print(lanche[-2]) # pizza
# # print(lanche[-2:]) # ('pizza', 'pudim')
# # print(lanche[1:3]) # ('suco', 'pizza')
# # print(lanche[2:]) # ('pizza', 'pudim')
# # print(lanche[:2]) # ('hamburguer', 'suco')

# for c in lanche:
#     print(f'Eu vou comer {c}.')

# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]} que está na posição {cont}.')
# print('Comi demais...')

# for pos, c in enumerate(lanche):
#     print(f'Eu vou comer {c} que está na posição {pos}.')
# print('Comi demais...')

# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = a + b
# print(c) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(len(c)) # 7
# print(c.count(8)) # 1
# print(c.index(4)) # 2
# print(c.index(2, 4)) # 6
# print(c.index(5, 1)) # 1

pessoa = ('Mateus', 21, 'M', 1.78)
# del(pessoa) # Deleta a variável
print(pessoa)
