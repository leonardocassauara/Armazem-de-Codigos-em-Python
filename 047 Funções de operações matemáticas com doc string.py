def aumentar(num, au):
    """
    Aumento percental de um valor
    :param num: Valor
    :param au: Fator de aumento
    :return: Retorna o resultado aumentado
    """
    aumento = num * (1 + au/100)
    return aumento


def diminuir(num, di):
    """
    Redução percentual de um valor
    :param num: Valor
    :param di: Fato de redução
    :return: Retorna o resultado reduzido
    """
    diminui = num * (1 - di/100)
    return diminui


def dobro(num):
    """
    Multiplica o valor por 2
    :param num: Valor
    :return: Retorna o valor duplicado
    """
    dob = num * 2
    return dob


def metade(num):
    """
    Divide o valor por 2
    :param num: Valor
    :return: Retorna o valor dividido em duas partes
    """
    met = num / 2
    return met

