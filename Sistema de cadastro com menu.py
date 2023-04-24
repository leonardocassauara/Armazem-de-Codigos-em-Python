from time import sleep
import os

def sistema_cadastro():
    if os.path.exists('dados.txt'):
        with open('dados.txt', 'r') as f:
            informacao_salva = f.read()
            lista = eval(informacao_salva)
    else:
        lista = []
    while True:
        cadastro = []
        print('━'*40)
        print('MENU PRINCIPAL'.center(40))
        print('━'*40)
        print('\033[0:33m1\033[m ─ \033[0:34mVer pessoas cadastradas\033[m\n'
              '\033[0:33m2\033[m ─ \033[0:34mCadastrar nova pessoa\033[m\n'
              '\033[0:33m3\033[m ─ \033[0:34mSair do programa\033[m')
        print('━'*40)
        try:
            menu = int(input('\033[0:32mSua opção: \033[m'))
        except TypeError:
            print('\033[0:31mERRO: Digite uma opção válida!\033[m')
        except ValueError:
            print('\033[0:31mERRO: Digite uma opção válida!\033[m')
        else:
            if menu == 1:
                print('━' * 40)
                print('PESSOAS CADASTRADAS'.center(40))
                print('━' * 40)
                for index, elemento in enumerate(lista):
                    print(f'{elemento[0]} \t\t\t\t\t{elemento[1]} anos')
            elif menu <= 0 or menu >= 4:
                print('\033[0:31mERRO: Digite uma opção válida!\033[m')
            elif menu == 2:
                x = str(input('Nome: '))
                while True:
                    try:
                        y = int(input('Idade: '))
                    except TypeError:
                        print('\033[0:31mERRO: por favor, digite um número inteiro válido.\033[m')
                    except ValueError:
                        print('\033[0:31mERRO: por favor, digite um número inteiro válido.\033[m')
                    else:
                        cadastro.append(x)
                        cadastro.append(y)
                        print(f'Novo registro de {x} adicionado.')
                        lista.append(cadastro[:])
                        break
            elif menu == 3:
                with open('dados.txt', 'w') as f:
                    f.write(str(lista))
                sleep(0.5)
                print('━' * 40)
                print('Saindo do sistema... Até logo!'.center(40))
                print('━' * 40)
                break


# Output:
sistema_cadastro()