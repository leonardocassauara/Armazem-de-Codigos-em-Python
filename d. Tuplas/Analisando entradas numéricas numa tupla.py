tupla_entradas_numericas = (int(input('Digite um número: ')),int(input('Digite mais um número: ')),int(input('Digite outro número: ')),int(input('Digite um último número: ')))

print(f'Você digitou os valores {tupla_entradas_numericas}\nO valor 9 apareceu {tupla_entradas_numericas.count(9)} vezes')
if 3 in tupla_entradas_numericas:
    print(f'O primeiro valor 3 apareceu na {tupla_entradas_numericas.index(3)+1}a posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end='')
for numero in tupla_entradas_numericas:
    if numero % 2 == 0:
        print(f'{numero}', end=' ')
