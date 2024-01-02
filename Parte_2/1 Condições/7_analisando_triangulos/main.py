r1 = float(input('Primeiro argumento: '))
r2 = float(input('Segundo argumento: '))
r3 = float(input('Terceiro argumento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar algum tipo de trinângulo!')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Os segmentos acima não podem formar um triângulo')