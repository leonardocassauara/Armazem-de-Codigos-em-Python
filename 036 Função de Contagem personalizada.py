from time import sleep

def contador(i,f,p):
    print('━'*30)
    if p < 0:
        p = p * -1
    elif p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        for c in range(i,f+1,p):
            print(f'{c}',end=' ')
            sleep(0.5)
    elif i > f:
            for c in range(i,f-1,-p):
                print(f'{c}',end=' ')
                sleep(0.5)
    elif i == f:
        print(i, end=' ')
    print('FIM!')


# Output:
contador(1,10,1)
contador(10,0,2)
print('━'*30)
print('Agora é a sua vez de personalizar a contagem!')
início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(início,fim,passo)
