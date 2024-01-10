palavras = ('Python', 'JavaScript', 'Machine Learning', 'Blockchain', 'API', 'Cybersecurity', 'Cloud Computing', 'Artificial Intelligence', 'Big Data', 'DevOps')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')