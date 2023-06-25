num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Para o número {} \n Sua unidade é {}\n Sua dezena  é {}\n Sua centena é {}\n Seu milhar  é {}'.format(num, u, d, c, m))

# Programa pode ser aprimorado com uso de loop 'for' ou 'while' para ajustar o limite das casas.
