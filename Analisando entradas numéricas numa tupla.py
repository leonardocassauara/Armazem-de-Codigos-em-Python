tupla = (int(input('Digite um número: ')),int(input('Digite mais um número: ')),int(input('Digite outro número: ')),int(input('Digite um último número: ')))
lista = []
c = 0
for c in range(0, 4):
    if tupla[c] % 2 == 0:
        lista.append(tupla[c])
print(f'Você digitou os valores {tupla}\nO valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)}a posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram {lista}')
