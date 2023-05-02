from random import randint
print('='*30)
print('ÍMPAR OU PAR'.center(30))
print('='*30)
contador_win = 0
while True:
    player = int(input('Diga um valor: '))
    modo = str(input('Par ou Ímpar? [P/I] ')).strip().upper().replace(' ','')
    pc = randint(1,10)
    print('-'*30)
    if (pc + player) % 2 == 0:
        if modo == 'P':
            print(f'Você jogou {player} e o computador jogou {pc}. Total de {pc + player} deu PAR')
            contador_win += 1
        elif modo == 'I':
            print(f'Você jogou {player} e o computador jogou {pc}. Total de {pc + player} deu ÍMPAR\nVocê venceu {contador_win} vezes.\n','-'*30)
            break
    elif (pc + player) % 2 != 0:
        if modo == 'I':
            print(f'Você jogou {player} e o computador jogou {pc}. Total de {pc + player} deu ÍMPAR')
            contador_win += 1
        elif modo == 'P':
            print(f'Você jogou {player} e o computador jogou {pc}. Total de {pc + player} deu PAR\nVocê venceu {contador_win} vezes.\n',('-'*30).ljust(30))
            break
    print('-'*30)
print('Fim de jogo!')
