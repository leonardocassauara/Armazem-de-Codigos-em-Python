soma = 0
tudo = list()
    # Loop:
while True:
    resp = ' '
    dicio = dict()
    dicio['NOME'] = str(input('Nome do Jogador: '))
    dicio['PARTIDAS'] = int(input(f'Quantas partidas {dicio["NOME"]} jogou? '))
    dicio['GOLS'] = []
    dicio['TOTAL'] = soma
    for c in range(0, dicio["PARTIDAS"]):
        dicio["GOLS"].append(int(input(f'Quantos gols na partida {c}? ')))
        soma += dicio["GOLS"][c]
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip().replace(' ','')[0]
    tudo.append(dicio.copy())
    print('─'*30)
    if resp in 'Nn':
        break
print('─'*40)
print(f'{"No.":<4}{"Nome":>4}{"Gols":>12}{"Total":>18}')
print('─'*40)
for index, elemento in enumerate(tudo):
    print(f'{index}  {elemento["NOME"]}     {elemento["GOLS"]}   \t\t\t{elemento["TOTAL"]}')
print('-'*40)
while True:
    n = int(input('Mostrar dados de qual jogador? (999 interrompe) '))
    if n == 999:
        print('<< VOLTE SEMPRE >>')
        break
    else:
        if n in range(0, len(tudo)):
            print(f'── LEVANTAMENTO DO JOGADOR {tudo[n]["NOME"]}:')
            for c in range(0, tudo[0]["PARTIDAS"]):
                print(f'  No jogo {c} fez {tudo[n]["GOLS"][c]}')
        else:
            print(f'ERRO! Não existe jogador com código {n}! Tente Novamente')
    print('─'*40)
