col = list()
for c in range(0, 3):
    col.append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0, 3):
    col.append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0, 3):
    col.append(int(input(f'Digite um valor para [2, {c}]: ')))
print('-'*30)
print(f'''[  {col[0]}  ] [  {col[1]}  ] [  {col[2]}  ]
[  {col[3]}  ] [  {col[4]}  ] [  {col[5]}  ] 
[  {col[6]}  ] [  {col[7]}  ] [  {col[8]}  ]''')