# Criação de lista + loop for para adicionar elementos a lista a partir de uma entrada
valor = list()
for c in range(0,5):
    valor.append(int(input(f'Digite um valor para a posição {c}: ')))

# Formatação + output, saída ou resultado
print('='*30)
print(f'Você digitou os valores {valor}')

# Encontrar os valores requisitados
b = valor[:]
maior = sorted(b)[-1]
menor = sorted(b)[0]


print(f'O menor valor foi {menor} nas posições: ', end='')

# Descobrir posição do menor:
for pos, key in enumerate(valor):
    if key == menor:
        print(f'{pos}', end= ' ')

print(f'\nO maior valor foi {maior} nas posições: ', end='')

# Descobrir posição do maior:
for pos, key in enumerate(valor):
    if key == maior:
        print(f'{pos}', end= ' ')
