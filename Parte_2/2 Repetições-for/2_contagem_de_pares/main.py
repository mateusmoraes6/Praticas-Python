for c in range(0, 50):
    print('.', end='')
    if c %2 == 0:
        print(c, end='')

# Forma mais eficiente ocupando metade do tempo
for d in range(2, 51, 2):
    print('.', end='')
    print(d, end='')