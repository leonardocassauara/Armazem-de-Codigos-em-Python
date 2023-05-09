n = str(input('Digite o seu ano: '))
p = int(n)
if p % 4 == 0 and p % 100 != 0 or p % 400 == 0:
    print('O seu ano é bissexto.')
else:
    print('O seu ano não é bissexto.')
