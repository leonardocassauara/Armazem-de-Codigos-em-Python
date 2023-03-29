# Programa que sorteia os números de um jogo de Mega Sena além de perguntar quantos jogos de 6 palpites serão sorteados:

# Apresentação
print('─'*36)
print('{:^36}'.format('JOGO NA MEGA SENA'))
print('─'*36)
numjogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('{:=^37}'.format(' SORTEANDO {} JOGOS ').format(numjogos))

# Sorteador de números
from time import sleep
from random import randint
for i in range(1, numjogos+1):
    lista = list()
    while len(lista) < 6:
        n = randint(0, 60)
        if n not in lista:
            lista.append(n)
    lista.sort()
    print(f'Jogo {i}: {lista}')
    lista.clear()
    sleep(0.5)
print('{:=^36}'.format(' < BOA SORTE! > '))
