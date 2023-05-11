lista = list()
contador = 0
while True:
    loop_lista = ' '
    contador += 1
    num = int(input('Digite um valor: '))
    lista.append(num)
    while loop_lista not in 'SsNn':
        loop_lista = str(input('Quer continuar? [S/N] ')).strip().replace(' ','')[0]
    if loop_lista in 'Nn':
        break
lista.sort(reverse=True)
print('='*30)
print(f'Você digitou {contador} elementos.',f'\nOs valores em ordem decrescente são {lista}', end='')
if 5 in lista:
    print('\nO valor 5 faz parte dessa lista!', end=' ')
else:
    print('\nO valor 5 não faz parte dessa lista!', end=' ')
