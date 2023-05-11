from random import choice
print('\033[1:35:1mVamos jogar Jokenpô.\033[m')
lista = ['pedra', 'papel', 'tesoura']
pc = choice(lista)
while True:
    a = input('\033[1:97:1mVou pensar numa jogada. Faça sua escolha!\n Pedra, papel, tesoura... \033[m')
    a = a.lower()
    if 'tesoura' in a or 'papel' in a or 'pedra' in a:
        if pc == a:
            print('\033[1:34:1mEmpatamos! Pensei em {} assim como você. Vamos de novo!\033[m'.format(pc))
        else:
            if pc == 'pedra' and a == 'papel':
                print('\033[1:32:1mParabéns! Você me venceu! \nEu pensei em {} e você em {}.\033[m'.format(pc, a))
                break
            elif pc == 'pedra' and a == 'tesoura':
                print('\033[1:31:1mAha! Eu venci! Eu pensei em {} e você em {}.\033[m'.format(pc, a))
                break
            elif pc == 'papel' and a == 'pedra':
                print('\033[1:31:1mAha! Eu venci! Eu pensei em {} e você em {}.\033[m'.format(pc, a))
                break
            elif pc == 'papel' and a == 'tesoura':
                print('\033[1:32:1mParabéns! Você me venceu! \nEu pensei em {} e você em {}.\033[m'.format(pc, a))
                break
            elif pc == 'tesoura' and a == 'pedra':
                print('\033[1:32:1mParabéns! Você me venceu! \nEu pensei em {} e você em {}.\033[m'.format(pc, a))
                break
            elif pc == 'tesoura' and a == 'papel':
                print('\033[1:31:1mAha! Eu venci! Eu pensei em {} e você em {}.\033[m'.format(pc, a))
                break
