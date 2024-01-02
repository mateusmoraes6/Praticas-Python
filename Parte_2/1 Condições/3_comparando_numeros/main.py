primeiroValor = int(input('Digite um valor: '))
segundoValor = int(input('Digite um valor: '))

if primeiroValor > segundoValor:
    print('O primeiro valor ({}) é maior que o segundo valor ({})!'.format(primeiroValor, segundoValor))
elif primeiroValor < segundoValor:
    print('O segundo valor ({}) é maior que o primeiro valor ({})!'.format(segundoValor, primeiroValor))
else:
    print('Ambos os valores são iguais, sendo: Primeiro Valor ({}) e Segundo Valor ({}).'.format(primeiroValor, segundoValor))
