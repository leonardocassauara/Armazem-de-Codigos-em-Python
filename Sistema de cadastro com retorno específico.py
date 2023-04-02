todos = list()
mulheres = list()
acima = list()
sid = 0

# Loop:
while True:
    resp = ' '
    dados = dict()
    dados["NOME"] = str(input('Nome: '))
    dados["IDADE"] = int(input('Idade: '))
    dados["SEXO"] = ' '
    sid += dados["IDADE"]
    while dados["SEXO"] not in 'MmFf':
        dados["SEXO"] = str(input('Sexo: [M/F] ')).strip().replace(' ','')[0]
    todos.append(dados.copy())
    if dados["SEXO"] in 'Ff':
        mulheres.append(dados["NOME"][:])
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip().replace(' ','')[0]
    if resp in 'Nn':
        break
média = sid / len(todos)
for index,elemento in enumerate(todos):
    if todos[index]["IDADE"] > média:
        acima.append(elemento)
print('─'*60)
print(f' ─ O grupo tem {len(todos)} pessoas.\n'
      f' ─ A média de idade do grupo é de {média:.2f}\n'
      f' ─ As mulheres cadastradas foram: {mulheres}\n'
      f' ─ Lista das pessoas que estão com IDADE acima da MÉDIA:\n')
for elemento in acima:
    print(f'{elemento}')
    print()
