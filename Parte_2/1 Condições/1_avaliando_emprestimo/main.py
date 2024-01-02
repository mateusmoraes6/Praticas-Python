nomeComprador = str(input('Qual o seu nome? '))
valorDaCasa = float(input('Informe o valor da casa: R$ '))
salario = float(input('Informe o seu salário: R$ '))
anosPagamento = int(input('Em quantos anos você pretende pagar? '))

print('Olá, {}, me confirma suas informações, então você deseja comprar uma casa no valor de R$ {:.3f}, sendo que seu salário é de R$ {:.3f} e pretende quitar em até {} anos...'.format(nomeComprador, valorDaCasa, salario, anosPagamento))

confirma = str(input('Certo? '))

print('Ok, estou avaliando!')

prestacaoAnual = valorDaCasa / anosPagamento

prestacaoMensal = prestacaoAnual / 12

print('Então, dentro desses {} anos, você irá pagar anualmente um total de R$ {:.3f} e mensalmente você pagará um total de R$ {:.3f}.'.format(anosPagamento, prestacaoAnual, prestacaoMensal))

exceder = (30 / 100) * salario + prestacaoMensal
print('Cálculo de excedência: R$ {:.3f}'.format(exceder))

if (exceder > salario) :
    print('Empréstimo negado! O valor de pagamento mensal excedeu o seu salário em 30%, que é o nosso limite.')
else :
    print('Empréstimo aprovado!')