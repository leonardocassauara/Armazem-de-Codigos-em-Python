def fatorial(num=1,show=False):
    """
    -> Calcula o fatorial de um número, mostrando ou não o cálculo
    :param num: O número a ser calculado
    :param show: 'True' ou 'False', (opcional) para mostrar o cálculo
    :return: sem retorno
    """
    print('━'*30)
    fatorial = 1
    for c in range(num, 0, -1):
        fatorial *= c
        if show:
            print(f'{c}',end='')
            print(' x ' if c > 1 else ' = ',end='')
    print(fatorial)


# Programa Principal:
fatorial(5, show=False)
fatorial(5, show=True)
fatorial()
fatorial(0, show=False)
fatorial(10, show=True)
