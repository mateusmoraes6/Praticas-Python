# num = int(input('Digite um número para ver sua tabuada: '))
# m = 10
# for c in range(0, m+1):
#     c *= num
#     print(c)

# Forma mais enxuta ainda
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))