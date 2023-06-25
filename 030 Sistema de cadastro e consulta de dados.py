# Variaveis e listas:
lista_tudo = list()
nome = list()
notas = list()
n = 0
    # Lista_tudo => nome => notas

# ‘Loop’ e sistema de listas para armazenar as notas e nomes de todas as pessoas digitadas
while True:
    continuacao = ' '
    vnome = str(input('Nome: '))
    nota_1 = float(input('Primeira nota: '))
    nota_2 = float(input('Segunda nota: '))
    notas.append(nota_1)
    notas.append(nota_2)
    nome.append(vnome)
    nome.append(notas[:])
    lista_tudo.append(nome[:])
    notas.clear()
    nome.clear()
    while continuacao not in 'SsNn':
        continuacao = str(input('Quer continuar? [S/N] ')).strip().replace(' ','')[0]
    if continuacao in 'Nn':
        break
print('-='*30)
print('No.   NOME              MÉDIA')
print('─'*30)
for index, key in enumerate(lista_tudo):
    print(f'{index}  {key[0]:<10}', f'{(key[1][0]+key[1][1])/2:>13}')
print('─'*30)

# Mostrar notas de um aluno específico com base no valor do index do enumerate
while n != 999:
        n = int(input('Mostrar notas de qual aluno? Digite o número dele (999 interrompe): '))
        print('─' * 30)
        print(f'Notas de {lista_tudo[n][0]} são {lista_tudo[n][1][0]} e {lista_tudo[n][1][1]}')
        print('─'*30)
