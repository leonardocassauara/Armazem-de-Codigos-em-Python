print('\033[1:33:1mBem vindo ao programa de base de conversão.\033[m')
while True:
    num = input('\033[1:36:1mPara iniciar, digite um número inteiro qualquer: \033[m')
    if num.isnumeric():
        base = input('\033[1:36:1m 1 - Para Binário \n 2 - Para Octal \n 3 - Hexadecimal \n  Digite a base de conversão: \033[m')
        if base.isnumeric():
            base = int(base)
            num = int(num)
            if base == 1:
                d = bin(num)                    # Converter para Binário
                print('\033[1:32:1m  O seu número {} convertido para Binário vira {}\033[m'.format(num, d[3:]))
                break
            elif base == 2:
                d = oct(num)                    # Converter para Octal
                print('\033[1:32:1mO seu número {} convertido para Octal vira {}\033[m'.format(num, d))
                break
            elif base == 3:
                d = hex(num)                    # Converter para Hexadecimal
                print('\033[1:32:1mO seu número {} convertido para Hexadecimal vira {}\033[m'.format(num, d))
                break
print('\033[1:33:1m  Obrigado por usar o programa de base de conversão.\033[m')
