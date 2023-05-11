# Função:
def maior(*num):
    print('━'*30)
    tamanho = len(num)
    print(f'{num} | Foram informados {tamanho} valores \nO MAIOR valor informado foi {max(num)}')


#Output:
maior(4,7,0)
maior(1)
maior(4,7,8,9,0,1,23)
