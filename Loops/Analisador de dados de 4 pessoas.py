d = 0
idade_s = 0
maior_idade_m = 0
e = 0
velho = 'place_holder'
b = False
for c in range(1, 5):
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo(F/M): ')).upper()
    idade_s += idade
    if sexo == 'M' and d == 0:
        d += 1
        maior_idade_m = idade
        velho = nome
        b = True
    elif sexo == 'M' and d != 0 and idade > maior_idade_m:
        velho = nome
        b = True
    elif sexo == 'F' and idade < 20:
        e += 1
média = idade_s / 4
if b is True:
    print('A média das idades do grupo é {:.1f} \nO homem mais velho se chama {} \nNo grupo, há {} mulheres com menos de 20 anos'.format(média, velho.title(), e))
else:
    print('A média das idades do grupo é {:.1f} \nNão há homens no grupo \nNo grupo, há {} mulheres com menos de 20 anos'.format(média, e))
