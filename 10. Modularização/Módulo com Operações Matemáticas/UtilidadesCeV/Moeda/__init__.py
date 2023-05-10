def moeda(valor):
    """
    Formata o valor para a moeda (R$)
    :param valor: Valor
    :return: Retorna o valor formatado
    """
    txt = 'R$' + ('{:.2f}'.format(valor)).replace('.',',')
    return txt


def aumentar(num, au, form=True):
    """
    Aumento percental de um valor
    :param form: (opicional) Mostra o valor formatado
    :param num: Valor
    :param au: Fator de aumento
    :return: Retorna o resultado aumentado
    """
    aumento = num * (1 + au/100)
    if form:
        return moeda(aumento)
    return aumento


def diminuir(num, di, form=True):
    """
    Redução percentual de um valor
    :param form: (opicional) Mostra o valor formatado
    :param num: Valor
    :param di: Fato de redução
    :return: Retorna o resultado reduzido
    """
    diminui = num * (1 - di/100)
    if form:
        return moeda(diminui)
    return diminui


def dobro(num, form=True):
    """
    Multiplica o valor por 2
    :param form: (opicional) Mostra o valor formatado
    :param num: Valor
    :return: Retorna o valor duplicado
    """
    dob = num * 2
    if form:
        return moeda(dob)
    return dob


def metade(num, form=True):
    """
    Divide o valor por 2
    :param form: (opicional) Mostra o valor formatado
    :param num: Valor
    :return: Retorna o valor dividido por 2
    """
    met = num / 2
    if form:
        return moeda(met)
    return met


def resumo(num, au, di):
    """
    Tabela formatada motrando valor, dobro, metade, aumento % e redução %
    :param num: Valor
    :param au: Fator de aumento
    :param di: Fator de redução
    :return: Sem retorno
    """
    print('━'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('━'*30)
    print('{:<16}'.format('Preço analisado:'),'  {}'.format(moeda(num)))
    print('{:<15}'.format('Dobro do preço:'),'   {}'.format(dobro(num)))
    print('{:<16}'.format('Metade do preço:'),'  {}'.format(metade(num)))
    print('{:<15}'.format('{}% de aumento:').format(au),'   {}'.format(aumentar(num,au)))
    print('{:<15}'.format('{}% de redução:').format(di),'   {}'.format(diminuir(num, di)))
    print('━'*30)
