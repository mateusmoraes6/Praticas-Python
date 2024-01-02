from datetime import datetime

diaNascimento = int(input('Informe somente o DIA do nascimento: '))
mesNascimento = int(input('Informe somente o MÊS de nascimento: '))
anoNascimento = int(input('Informe somente o ANO de nascimento: '))

dataAtual = datetime.now()

# Calculando a idade por completo
idadeAnos = dataAtual.year - anoNascimento

dataNascimentoAjustada = datetime(dataAtual.year, mesNascimento, diaNascimento)
diferenca = dataAtual - dataNascimentoAjustada

idadeMeses = diferenca.days // 30
idadeDias = diferenca.days % 30

print(f"idade: {idadeAnos} anos, {idadeMeses} meses e {idadeDias} dias.")

# Calcular a idade que falta para completar 18 anos
idadeFaltando = 18 - idadeAnos

# Calculando a data que se completa 18 anos
dataCompleta18 = datetime(dataAtual.year + idadeFaltando, mesNascimento, diaNascimento)

# Calculando diferença em dias até completar 18 anos
diferenca18 = dataCompleta18 - dataAtual
diasFaltando = diferenca18.days


if (idadeAnos > 45) :
    print('Sinto muito, meu caro, mas você já passou da idade para se alistar!')
elif (idadeAnos >= 18) :
    print('Você está na idade para se alistar, vamos arrumar esses documentos!?')
else :
    print('Meu jovem, você ainda não atingiu a idade permitida para se alistar, ainda lhe faltam {} anos e {} dias para você completar 18 anos, fique de olho, quando essa data chegar ao fim, pode voltar aqui!'.format(idadeFaltando, diasFaltando))