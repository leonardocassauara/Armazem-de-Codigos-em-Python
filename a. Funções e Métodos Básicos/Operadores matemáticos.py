n1 = float(input('Digite sua nota do primeiro bimestre: '))
n2 = float(input('Digite sua nota do segundo bimestre: '))
média = (n1 + n2)/2
raiz_1 = n1 ** 0.5
raiz_2 = n2 ** 0.5
dobro_1 = n1 * 2
dobro_2 = n2 * 2
triplo_1 = n1 * 3
triplo_2 = n2 * 3
antecessor_1 = n1 - 1
sucessor_1 = n1 + 1
antecessor_2 = n2 - 1
sucessor_2 = n2 + 1
print(f'Para o primeiro valor: raiz quadrada = {raiz_1:.2f} | dobro = {dobro_1:.0f} | triplo = {triplo_1:.0f} | antecessor = {antecessor_1:.0f} | sucessor = {sucessor_1:.0f}\n'
      f'Para o segundo  valor: raiz quadrada = {raiz_2:.2f} | dobro = {dobro_2:.0f} | triplo = {triplo_2:.0f} | antecessor = {antecessor_2:.0f} | sucessor = {sucessor_2:.0f}\n'
      f'Média entre ambos os valores: {média}')
