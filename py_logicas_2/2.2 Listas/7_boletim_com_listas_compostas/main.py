dados = list()
alunos = list()
cont = 0
while True:
    nome = (str(input('Nome: ')))
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))

    media = (nota1 + nota2) / 2

    dados.append(nome)
    dados.append(nota1)
    dados.append(nota2)
    dados.append(media)

    alunos.append(dados[:])
    dados.clear()

    cont += 1
    continua = str(input('Quer continuar? [S/N] '))
    if continua in 'Nn':
        break
print('-='*10)
print('No.    Nome        Média')
print('-'*25)
for i, pos in enumerate(alunos, 1):
    print(f'{i:<5} {pos[0]:<12} {pos[3]:4.2f}')

while True:
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if notas == 999:
        break
    if i <= notas <= len(alunos):
        pos = alunos[notas - i]
        print(f'Notas de {pos[0]}: {pos[1]:.2f} e {pos[2]:.2f}.')
    else:
        print('Valor inválido!')