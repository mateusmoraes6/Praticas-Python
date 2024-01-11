valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
print('-'*40)
print(f'Você digitou os valores: {valores}.')
print(f'O maior valor digitado foi {max(valores)} na posição: {valores.index(max(valores))}', end='... ')
print(f'\nO menor valor digitado foi {min(valores)} na posição: {valores.index(min(valores))}', end='... ')