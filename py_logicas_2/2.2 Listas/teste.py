# teste = list()
# teste.append('Mateus')
# teste.append(21)
# pessoas = list()
# pessoas.append(teste[:])
# teste[0] = 'Jão'
# teste[1] = 22
# pessoas.append(teste[:])
# print(pessoas)

# galera = [['João', 24], ['Ana', 28], ['Joaquim', 25], ['Maria', 32]]
# print(galera[0][0])
# print(galera[2][1])
# # for p in galera:
# #     print(p[0])
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')