print('Programa que calcula a média de apenas 2 avaliações.')
nota1 = float(input('Informe a sua nota: '))
nota2 = float(input('Informe a sua nota: '))

notaMedia = ((nota1 + nota2) / 2)
print('Sua nota foi: {}'.format(notaMedia))

if notaMedia < 5.0:
    print('REPROVADO!')
elif notaMedia == 5.0 or 6.9:
    print('RECUPERAÇÃO!')
elif notaMedia >= 7:
    print('APROVADO!')