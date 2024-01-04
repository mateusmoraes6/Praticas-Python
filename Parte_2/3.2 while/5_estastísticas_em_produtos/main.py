preçoTot = valorMax = valorMin = cont = 0
continua = 'S'
while continua == 'S':
    # produto = str(input('Nome do produto: '))
    preço = int(input('Preço: R$'))
    if preço >= 1000:
        valorMax += 1
    preçoTot += preço
    cont = preço
    continua = str(input('Quer continuar? [S/N] ')).upper()
   
print(f'''FIM DO PROGRAMA
Total da compra: R${preçoTot:.2f}.
Total de produtos custando R$1000.00 ou mais: {valorMax}.
O produto mais barato foi {cont} que custa R$.''')

# Ainda estou finalizando.