n = s = 0
cont = 1
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Você digitou {cont} números e a soma desses números foi {s}.')