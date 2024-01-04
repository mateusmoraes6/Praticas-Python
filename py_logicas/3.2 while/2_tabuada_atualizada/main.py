from time import sleep
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 35)
    cont = 1
    while cont <= 10 and n > 0:
        mult = cont * n
        sleep(0.2)
        print(f'{n} x {cont} = {mult}')
        cont += 1
    if n <= 0:
        print('TABUADA ENCERRADA. Volte quando quiser!')
        break
