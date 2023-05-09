# Matriz, 3x3 de listas, preenchida com valores obtidos pelo input:

Matriz = list()
dados = list()
linha = 0
coluna = 0
soma_par = 0
soma_coluna3 = 0
e = 0

# Print:
# São 9 entradas de valores
for c in range(0,9):
    n = int(input(f'Digite o valor da posição [{linha}, {coluna}]: '))
    coluna += 1
    if coluna == 3:
        linha += 1
        coluna = 0
    # Até agora o programa acima serviu para declarar variaveis e formatar o print
    # Transformar os valores obtidos pelo 'n' nos elementos da matriz
    dados.append(n)
    if len(dados) == 3:
        Matriz.append(dados[:])
        dados.clear()
print('-='*30)
print(f'{Matriz[0]}',f'\n{Matriz[1]}',f'\n{Matriz[2]}')

# A soma de todos os valores pares digitados:
while e < 3:
    for numero in Matriz[e]:
        if numero % 2 == 0:
            soma_par += numero
    e += 1

# A soma dos valores da 3ª coluna:
soma_coluna3 = Matriz[0][2] + Matriz[1][2] + Matriz[2][2]

# O maior valor da 2ª linha:
maior_2linha = max(Matriz[1])

# Formatação do print:
print(f'A soma dos valores pares é {soma_par}\nA soma dos valores da terceira coluna é {soma_coluna3}\nO maior valor da segunda linha é {maior_2linha}')
