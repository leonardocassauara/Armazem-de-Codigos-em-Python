palavras = ('Tomate', 'Limao', 'Abacaxi', 'Pizza')
vogais = ('a', 'e', 'i', 'o', 'u')

for elemento in palavras:
    print(f'\nNa palavra {elemento.title()}\t temos',end=' ')
    for letra in vogais:
        if letra in elemento:
            print(letra,end=' ')
