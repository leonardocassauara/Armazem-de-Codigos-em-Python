from datetime import date
print('Bem vindo a interface da Confederação Nacional de Natação.')
dia = date.today().day
mês = date.today().month
ano = date.today().year
while True:
    dia_c = input('Digite o dia(DD) em que nasceu: ')
    mês_c = input('Digite o mês(MM) em que nasceu: ')
    ano_c = input('Digite o ano(AAAA) em que nasceu: ')
    if dia_c.isnumeric() and mês_c.isnumeric() and ano_c.isnumeric():
        dia_c = int(dia_c)
        mês_c = int(mês_c)
        ano_c = int(ano_c)
        Zero_ou_um = bool((dia, mês) < (dia_c, mês_c))
        idade = (ano - ano_c) - Zero_ou_um
        if 4 < idade <= 9:
            print('Você tem {} anos e está classificado para a categoria MIRIM'.format(idade))
            break
        elif 9 < idade <= 14:
            print('Você tem {} anos e está classificado para a categoria INFANTIL'.format(idade))
            break
        elif 14 < idade <= 19:
            print('Você tem {} anos e está classificado para a categoria JUNIOR'.format(idade))
            break
        elif idade == 20:
            print('Você tem {} anos e está classificado para a categoria SENIOR'.format(idade))
            break
        else:
            print('Você tem {} anos e está classificado para a categoria MASTER'.format(idade))
            break
