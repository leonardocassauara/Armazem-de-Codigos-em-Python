print('─'*30, '\nSequência de Fibonacci')
print('─'*30)
termos = int(input('Quantos termos você quer mostrar? '))
lista = [0, 1]
contador = 2
a = 0
t1 = 0
t2 = 1
t3 = 0
print('{} | {} | '.format(t1, t2), end='')
while contador != termos:
    t3 = t1 + t2
    print('{}'.format(t3), end='')
    print(' | ' if contador < termos - 1 else ' | FIM', end='')
    t1 = t2
    t2 = t3
    contador += 1
