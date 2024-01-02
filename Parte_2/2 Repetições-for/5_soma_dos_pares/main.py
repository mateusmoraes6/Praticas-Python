soma = 0
cont = 0
for c in range(0, 6):
    valores = int(input('Digite um valor inteiro: '))
    if valores %2 == 0:
        cont += 1
        soma += valores
print('Você informou {} números pares e sua soma foi: {:.2f}'.format(cont, soma))