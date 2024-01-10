listagem = ('Lápis', 1.70,
             'Borracha', 2, 
             'Frango', 10.90,
             'Caderno', 15.90,
             'Estojo', 2,
             'Transferidor', 4.20,
             'Compasso', 9.99,
             'Mochila', 89.90,
             'Canetas', 22.30,
             'Livros', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PTRÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 ==0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)
