from random import randint
n = randint(0, 100)                                  # Número aleatório de 0 a 100 que computador vai pensar.
print('\033[1:33:1mVou pensar em um número de 0 a 100, incluindo esses.\nSerá que você consegue advinha-lo em 10 tentativas?\033[m')
HP = 10             # Tentativas de acertos, vidas.
chutes = 0          # Palpites.
while chutes != n:                                   # "Enquanto os palpites forem diferentes do número escolhido:"
    chutes = input('Dê o seu palpite: ')             # Os palpites são as respostas desse input
    if chutes.isnumeric():                           # "Se os palpites forem valores numericos, os palpites devem:"
        chutes = int(chutes)                         # "números inteiros."
        HP = HP - 1                                  # Todavia, para ter chegado até essa etapa, significa que o player errou o 'n', perdendo 1 de HP
        if chutes > n:
            print('\033[1:31:1mUm pouco mais baixo... \033[m')         # Dicas em relação ao valor do palpite, se é mais alto ou baixo.
        if chutes < n:
            print('\033[1:31:1mUm pouco mais alto... \033[m')
        if HP == 0:                                  # Sistema de vidas, a dificuldade depende do número de HP e do espaço amostral, nesse caso 100 números.
            print('\033[1:35:1mQue pena. Você esgotou todas as suas tentativas e perdeu.\nMais sorte da próxima vez!\033[m') # Derrota, o HP zerou.
            break
    if chutes == 'sair':                                               # Comando para fechar o minigame. Desnecessário? Talvez.
        print('\033[1:35:1mQue pena! O número que pensei era {}.\033[m'.format(n))
        break
else:
    print('\033[1:32:1mParabens! \nVocê adivinhou o número {}! \nE ainda tinha {} tentativas.\033[m'.format(n, HP))    # Vitória, mostrando o HP restante.
