print('━'*30)
print('Cadastre uma pessoa'.center(30))
print('━'*30)
maioridade = contador_homem = contador_mulher_20 = idade = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        maioridade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip().replace(' ','')[0]
    if sexo == 'F' and idade < 20:
        contador_mulher_20 += 1
    elif sexo == 'M':
        contador_homem += 1
    continuação = ' '
    print('━' * 30)
    while continuação not in 'SN':
        continuação = str(input('Quer continuar? [S/N] ')).upper().strip().replace(' ','')[0]
    if continuação == 'N':
        break
print('━'*10,'FIM DO PROGRAMA','━'*10)
print(f'Total de pessoas com mais de 18 anos: {maioridade}\nAo todo temos {contador_homem} homens cadastrados\nE temos {contador_mulher_20} mulheres com menos de 20 anos')
