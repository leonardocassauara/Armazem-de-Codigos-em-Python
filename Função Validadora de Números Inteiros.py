def leiaInt(entrada):
    """
    — > Valida se um número é inteiro
    :param entrada: número
    :return: valor do argumento
    """
    entrada = input('Digite um número inteiro: ')
    if '-' in entrada:
        if entrada.startswith('-') and entrada[1:].isnumeric():
            return entrada
    while not entrada.isnumeric():
        print('\033[1:31:1mERRO! Digite um número inteiro válido.\033[m')
        entrada = input('Digite um número inteiro: ')
        if '-' in entrada:
            if entrada.startswith('-') and entrada[1:].isnumeric():
                break
    return entrada


# Programa Principal:
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
