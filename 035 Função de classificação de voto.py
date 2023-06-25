def voto(dia, mes, ano):
    """
    — > Mostra um valor literal baseado na idade que classifica o voto
    :param dia: dia de nascimento
    :param mes: mês de nascimento
    :param ano: ano de nascimento
    :return: sem retorno
    """
    from datetime import date
    zero_ou_um = bool((mes,dia) > (date.today().month,date.today().day))
    idade = (date.today().year - ano) - zero_ou_um
    if idade >= 65:
        print(f'Com {idade} anos: VOTO OPICIONAL')
    elif 16 <= idade < 18:
        print(f'Com {idade} anos: VOTO OPICIONAL')
    elif 18 <= idade < 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    elif idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO')


# Programa Principal:
voto(18,3,2000)
voto(17,3,2000)
voto(1,8,1980)
voto(1,2,2006)
help(voto)
