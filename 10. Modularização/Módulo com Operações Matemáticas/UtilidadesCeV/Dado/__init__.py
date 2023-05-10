def leiadinheiro(entrada):
    while True:
        valor = str(input(entrada)).replace(',','.')
        x = valor.replace('.','').replace(',','')
        if x.isdigit():
            return float(valor)
        else:
            print(f'\033[0:31:1mERRO: "{valor}" é um preço inválido!\033[m')

