maior_peso = 0
menor_peso = 0
lista_tudo = list()
dados = list()

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))

    # Determinar gerenciamento de listas
    dados.append(nome)
    dados.append(peso)
    lista_tudo.append(dados[:])
    dados.clear()

    # Determinação dos valores extremos
    if len(lista_tudo) == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso

    # Condição para o 'loop' quebrar e se repetir
    cont = ' '
    while cont not in 'SsNn':
        cont = str(input('Quer continuar? [S/N] ')).strip().replace(' ','')[0]
    if cont in 'Nn':
        break

# Formatação e print:
print('-='*30)
print(f'Ao todo, você cadastrou {len(lista_tudo)} pessoas')
print(f'O maior peso foi {maior_peso}. Peso de ',end='')
for elemento in lista_tudo:
    if elemento[1] == maior_peso:
        print(f'{elemento[0]}',end=' ')
print(f'\nO menor peso foi {menor_peso}. Peso de ',end='')
for elemento in lista_tudo:
    if elemento[1] == menor_peso:
        print(f'{elemento[0]}',end=' ')
