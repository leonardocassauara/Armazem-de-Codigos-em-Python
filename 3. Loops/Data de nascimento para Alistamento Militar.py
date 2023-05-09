import datetime
dia = datetime.date.today().day
mes = datetime.date.today().month
year = datetime.date.today().year
print('Bem vindo ao programa de alistamento militar nacional. \nDigite os dados do questionário.')
print('─'*30)
while True:
    dia1 = input('Nasceu em que dia(DD)? ')
    mes1 = input('Em que mês(MM)? ')
    ano1 = input('Em qual ano(AAAA)? ')
    print('─'*30)
    if dia1.isnumeric() and mes1.isnumeric() and ano1.isnumeric():
        dia1 = int(dia1)
        mes1 = int(mes1)
        ano1 = int(ano1)
        print('A sua data de nascimento é: {} {} {}'.format(dia1, mes1, ano1))
        alistamento = ((dia - dia1) + ((mes - mes1)*31) + ((year - ano1)*31*12)) // 365
        if alistamento == 18:
            print('Está na hora de se alistar!')
            break
        elif alistamento < 18:
            print('Ainda não está na hora de se alistar. Falta(m) {} ano(s)'.format(18 - alistamento))
            break
        elif alistamento > 18:
            print('Acorda pra vida! Ja passou da hora de se alistar. Você está {} ano(s) atrasado'.format(alistamento - 18))
            break
print('Obrigado.')
