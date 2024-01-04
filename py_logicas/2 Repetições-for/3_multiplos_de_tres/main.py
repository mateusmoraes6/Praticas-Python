soma = 0
cont = 0
for c in range(0, 31):
    if c %3 == 0:
        cont += 1
        soma += c
        print(c) 
print('A soma de os {} valores solicitados é: {}'.format(cont, soma))
