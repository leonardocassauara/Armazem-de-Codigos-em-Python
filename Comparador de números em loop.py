dados = list()
resultado = list()
print('\033[1:35:1mCompare dois números...\033[m')
while True:
    cont = ' '
    a = input('\033[1:39:1mDigite um número: \033[m')
    b = input('\033[1:39:1mDigite outro número para comparação: \033[m')
    if a.isnumeric() and b.isnumeric():
        a = int(a)
        b = int(b)
        dados.append(a)
        dados.append(b)
        resultado.append(dados[:])
        dados.clear()
        if a == b:
            print('\033[1:34:1mAmbos os números digitados são iguais!\033[m')
            print('─'*30)
        elif a > b:
            print('\033[1:34:1mO número {} é maior que o número {}. Logo, o número {} é o menor\033[m'.format(a, b, b))
            print('─'*30)
        elif a < b:
            print('\033[1:34:1mO número {} é maior que o número {}. Logo o número {} é o menor.\033[m'.format(b, a, a))
            print('─'*30)
        while cont not in 'SsNn':
            cont = str(input('Quer continuar? [S/N] ')).strip().replace(' ','')[0]
        if cont in 'Nn':
            print(f'\033[1:34:1mVocê comparou as duplas:\033[m \033[1:32:1m{resultado}\033[m')
            break
