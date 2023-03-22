palavras = []
vogais = ('a', 'e', 'i', 'o', 'u')
while True:
    entrada = str(input('Digite uma palavra ou "FIM" para encerrar: ')).strip().title()
    if entrada == 'Fim':
        break
    palavras.append(entrada.lower())
for elemento in palavras:
    print(f'\nNa palavra {elemento.title()}, temos',end=' ')
    for letra in vogais:
        if letra in elemento:
            print(letra,end=' ')
