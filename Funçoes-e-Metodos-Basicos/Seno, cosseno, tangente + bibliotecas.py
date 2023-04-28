from math import radians, sin, cos, tan
ang = float(input('Digite um valor de ângulo: '))
x = radians(ang)
seno = sin(x)
coss = cos(x)
tangent = tan(x)
print('Para o ângulo {}°, temos: \n Seu SENO     igual a {:.2f} \n Seu COSSENO  igual a {:.2f} \n Sua TANGENTE igual {:.2f}'.format(ang, seno, coss, tangent))
