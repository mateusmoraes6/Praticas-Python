preçoTot = valorMax = cont = 0
valorMin = float('inf')
continua = 'S'
while continua == 'S':
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    if preço >= 1000:
        valorMax += 1
    preçoTot += preço
    if preço < valorMin:
        valorMin = preço
        produtoMaisBarato = produto
    continua = str(input('Quer continuar? [S/N] ')).upper()
print('-' * 30) 
print('       FIM DO PROGRAMA')  
print('-' * 30) 
print(f'''Total da compra: R${preçoTot:.2f}.
Total de produtos custando R$1000.00 ou mais: {valorMax}.
O produto mais barato foi {produtoMaisBarato} que custa R${valorMin:.2f}.''')
