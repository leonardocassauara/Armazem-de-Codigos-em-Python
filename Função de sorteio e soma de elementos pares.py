from random import randint
from time import sleep

# Função I:
def sorteia(dados):
    for c in range(0, 5):
        dados.append(randint(1,10))
    print('Sorteando 5 valores!')
    sleep(0.5)
    print(f'Os valores sorteados foram {dados}')
    sleep(0.5)


def somapar(lista):
    soma = 0
    for index, elemento in enumerate(lista):
        if elemento % 2 == 0:
            soma += elemento
    print(f'A soma dos elementos pares foi {soma}')


# Output:
numeros = list()
sorteia(numeros)
somapar(numeros)
