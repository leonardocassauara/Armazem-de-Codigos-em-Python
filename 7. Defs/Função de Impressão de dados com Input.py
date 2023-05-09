def ficha(nome='<desconhecido>',gols=0):
    """
    — > Recebe e mostra Nome Do Jogador e Número de Gols
    :param nome: nome do jogador
    :param gols: número de gols
    :return: sem retorno
    """
    print('━'*30)
    print(f'O jogador {nome} fez {gols} gols no campeonato')


# Programa principal
print('━' * 30)
nom = str(input('Nome do Jogador: '))
numgol = input('Número de Gols: ')
if numgol.isnumeric():
    numgol = int(numgol)
else: numgol = 0
if nom.strip() == '':
    ficha(gols=numgol)
else:
    ficha(nome=nom, gols=numgol)
