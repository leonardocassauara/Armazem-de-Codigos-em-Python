menu = 6
while menu != 5:
    num_1 = float(input('Digite um valor: '))
    num_2 = float(input('Digite outro valor: '))
    menu = int(input('Digite:\n[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do Programa\nDigite a sua resposta: '))
    if menu == 1:
        print('A soma de {:.0f} com {:.0f} é {:.0f}'.format(num_1, num_2, num_1 + num_2))
    elif menu == 2:
        print('O produto de {:.0f} com {:.0f} é {:.0f}'.format(num_1, num_2, num_1 * num_2))
    elif menu == 3:
        if num_1 > num_2:
            print('O maior valor é {:.0f}'.format(num_1))
        else:
            print('O maior valor é {:.0f}'.format(num_2))
