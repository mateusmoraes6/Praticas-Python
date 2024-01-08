todosValores = ()
for c in range(0, 4):
    valores = int(input('Digite algum número: '))
    todosValores += (valores,)
print(f'Você digitou os valores {todosValores}.')
print(f'O valor {todosValores[1]} apareceu {todosValores.count(todosValores[1])} vezes.')
print(f'O valor {todosValores[3]} apareceu na {todosValores.index(todosValores[3])+1}ª posição.')
valoresPares = []
for num in todosValores:
    if num %2 == 0:
        valoresPares.append(num)
print(f'Os valores pares digitadfos foram: {valoresPares}',end=' ')