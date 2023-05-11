print('─'*30)
print('Sequência de Fibonacci'.center(30))
print('─'*30)

contador = 0
termo_1 = 0
termo_2 = 1
termo_3 = 0

print(f'{termo_1} | {termo_2}\n', end='')

num_termos = int(input('Quantos termos a mais você quer mostrar? '))

while contador != num_termos:
    termo_3 = termo_1 + termo_2
    print('{}'.format(termo_3), end='')
    print(' | ' if contador < num_termos - 1 else ' | FIM', end='')
    termo_1 = termo_2
    termo_2 = termo_3
    contador += 1
