def textocor(mensagem, cor=0):
    cores = ('\033[m',         # 0 — Sem cor
             '\033[0:97:41m',  # 1 - Texto = Branco, Background = Vermelho
             '\033[0:97:42m',  # 2 - Texto = Branco, Background = Verde
             '\033[0:97:43m',  # 3 - Texto = Branco, Background = Amarelo
             '\033[0:97:44m',  # 4 - Texto = Branco, Background = Azul
             '\033[0:97:45m',  # 5 - Texto = Branco, Background = Magenta
             '\033[0:97:46m',  # 6 - Texto = Branco, Background = Ciano
             '\033[0:97:47m')  # 7 - Texto = Branco, Background = Cinza
    print(f'{cores[cor]}{mensagem}{cores[0]}')


# Programa teste:
textocor('Threat of the Invader',5)
