n = int(input('Digite um número qualquer: '))            # Número que o jogador dará como entrada
multiplos = 0                                            # Placeholder para o número de múltiplos
for c in range(2, n):                                    # Loop para determinar se existem múltiplos desse número n
    if n % c == 0:                                       # Aqui determinamos se algum número igual ou maior que 2 e menor que n são múltiplos de n
        multiplos += 1                                   # Se a condição for satisfeita, o valor da váriavel multiplos será diferente de 0, implicando que n não é primo
        print('O número {} é multiplo de {}'.format(n, c))
if multiplos == 0:
    print('O número {} é primo'.format(n))
else:
    print('='*27, '\nO número {} tem {} múltiplos'.format(n, multiplos))
    print('='*27)
