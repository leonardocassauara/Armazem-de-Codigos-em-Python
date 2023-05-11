def área(l,c):
    print(f'A área de um terreno de {l}x{c} vale {l*c} m²')


print('Controle de Terrenos')
print('─'*30)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
área(larg,comp)
