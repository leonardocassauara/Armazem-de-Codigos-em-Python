def leiaint(msg):
    while True:
        try:
            entrada = int(input(msg))
        except Exception as error:
            print(f'\033[0:31mERRO: por favor, digite um número válido. Código: {error.__cause__}\033[m')
            continue
        else:
            return entrada


def leiafloat(msg):
    while True:
        try:
            entrada = float(input(msg))
        except KeyboardInterrupt:
            return 0
        except Exception as error:
            print(f'\033[0:31mERRO: por favor, digite um número válido. Código: {error.__cause__}\033[m')
            continue
        else:
            return entrada

