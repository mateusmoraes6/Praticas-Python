# n = 1
# while n != 0:
#     sexo = str(input('Informe seu sexo [M/F]: ')).upper()
#     if sexo == 'M' or sexo == 'F':
#         print('Muito bem, sexo informado ({}).'.format(sexo))
#         break
#     else:
#         print('INVÁLIDO, insira novamente!')

# De outra forma mais simples

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))