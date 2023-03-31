from datetime import date

# Dicionário:
dicio = dict()

# Nome, dada de nascimento e CTPS:
    # Nome:
dicio['nome'] = str(input('Nome: '))

    # Idade:
dia = date.today().day
mes = date.today().month
ano = date.today().year
dia_entrada = int(input('Em que dia nasceu? '))
mes_entrada = int(input('Em que mês nasceu? [MM] '))
ano_entrada = int(input('Em que ano nasceu? [AAAA] '))
zeroum = bool((dia,mes)<(dia_entrada,mes_entrada))
dicio['idade'] = int(ano - ano_entrada) - zeroum

    # CTPS:
dicio['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if dicio['CTPS'] != 0:
    dicio['contratação'] = int(input('Ano de Contratação: '))
    dicio['salário'] = int(input('Salário: R$'))
    dicio['aposentadoria'] = (dicio['contratação'] + 35) - ano_entrada

# Print:
print('='*30)
print(dicio)
for index, elemento in dicio.items():
    print(f'{index} tem o valor {elemento}')
