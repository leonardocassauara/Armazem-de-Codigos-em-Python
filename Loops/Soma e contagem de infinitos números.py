contador = 1
n = int(input('Digite um valor (999 para parar): '))
soma = n
while n != 999:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        print(f'A soma dos {contador} valores foi {soma}')
        break
    contador += 1
    soma += n
