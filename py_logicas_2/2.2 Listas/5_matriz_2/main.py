col = list()
for c in range(0, 3):
    col.append(int(input(f'Digite um valor para [0, {c}]: ')))
    cont = col
# for c in range(0, 3):
#     col.append(int(input(f'Digite um valor para [1, {c}]: ')))
# for c in range(0, 3):
#     col.append(int(input(f'Digite um valor para [2, {c}]: ')))

print('-'*30)
print(f'''[  {col[0]}  ] [  {col[1]}  ] [  {col[2]}  ]
''')
print('-'*30)
