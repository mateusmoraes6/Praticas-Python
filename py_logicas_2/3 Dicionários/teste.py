# pessoas = {'Nome': 'Mateus', 'Sexo': 'M', 'Idade': 21 }
# print(pessoas['Nome']) # Mateus
# print(pessoas['Idade']) # 21
# print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')
# print(pessoas.keys()) # (['Nome', 'Sexo', 'Idade'])
# print(pessoas.values()) # (['Mateus', 'M', 21])
# print(pessoas.items()) # ([('Nome', 'Mateus'), ('Sexo', 'M'), ('Idade', 21)])
# for k in pessoas.keys():
#     print(k)
# for k in pessoas.values():
#     print(k)
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
# del pessoas['Sexo']
# pessoas['Nome'] = 'Cristiano Ronaldo'
# pessoas['Idade'] = 38
# pessoas['Peso'] = 83
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# brasil = []
# estado1 = {'UF': 'Espírito Santo', 'Sigla': 'ES'}
# estado2 = {'UF': 'Minas Gerais', 'Sigla': 'MG'}
# brasil.append(estado1)
# brasil.append(estado2)

# print(brasil)
# print(brasil[0]['UF']) # Espírito Santo
# print(brasil[1]['Sigla']) # MG

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    print(e)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
