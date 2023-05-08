def syspyhelp():
    from time import sleep
    while True:
        tam1 = len('SISTEMA DE AJUDA PYHELP')+4
        print('\033[m\033[0:97:42m━'*tam1)
        print('SISTEMA DE AJUDA PYHELP'.center(tam1))
        print('━'*tam1)
        comando = str(input('\033[mFunção ou Biblioteca (FIM para encerrar) > '))
        if comando == 'FIM' or comando == 'fim':
            tam3 = len('ATÉ LOGO!')+4
            print('\033[0:97:41m━'*tam3)
            print('ATÉ LOGO!'.center(tam3))
            print('━'*tam3)
            break
        tam2 = len(f'Acessando o Manual do comando {comando}')+4
        print('\033[0:97:44m━' * tam2)
        print(f'Acessando o Manual do comando {comando}'.center(tam2))
        print('━' * tam2)
        sleep(1)
        print(f'\033[1:30:107m',end='')
        help(comando)
    sleep(0.5)


# Output:
syspyhelp()
