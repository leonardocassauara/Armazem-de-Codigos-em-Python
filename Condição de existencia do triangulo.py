from math import fabs
a = float(input('Digite o valor de um lado do triângulo: '))
b = float(input('Digite outro valor: '))
c = float(input('Digite o último valor: '))
if fabs(b - c) < a < (b + c):
    print('Um triângulo pode ser criado com esses valores.')
else:
    print('Um triângulo não pode existir com esses valores.')

# A condição de existência de um triângulo é: um lado deve ser menor que a soma dos outros dois, e maior que o módulo da diferença entre os outros dois
