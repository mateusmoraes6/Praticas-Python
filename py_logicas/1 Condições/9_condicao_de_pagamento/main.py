print('{:=^40}'.format(' PAG TESTE '))
preçoDoProduto = float(input('Informe o preço da sua compra: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] Á vita dinheiro/cheque
[ 2 ] Á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
formaDePagamento = int(input('Qual é a opção?  '))

if formaDePagamento == 1:
    total = preçoDoProduto - (10 / 100)
elif formaDePagamento == 2:
    total = preçoDoProduto - (5 / 100)
elif formaDePagamento == 3:
    total = preçoDoProduto
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif formaDePagamento == 4:
    total = preçoDoProduto + (preçoDoProduto * 20 / 100)
    outrasParcelas = int(input('Quantas parcelas? '))
    parcela = total / outrasParcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS!'.format(outrasParcelas, parcela))
else:
    total = preçoDoProduto
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamenete!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preçoDoProduto, total))